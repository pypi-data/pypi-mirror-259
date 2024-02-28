import adal
import requests
import json
import parcadfc.parcadfc_aux as paux
import pandas as pd
import datetime
import os
import openpyxl
import hashlib

import adal  # Asegúrate de tener instalada la librería adal
from bs4 import BeautifulSoup

def get_token(tenant_id, client_id, key_value):
    """
    Realiza un inicio de sesión en la API de Azure Defender for Cloud para realizar consultas, utilizando claves de acceso.

    Referencia: https://adal-python.readthedocs.io/en/latest/#adal.AuthenticationContext.acquire_token_with_client_credentials

    :param tenant_id: Identificador del Tenant de Azure al que se desea conectar.
    :param client_id: Cadena que indica el ID de la clave de acceso (Access Key ID).
    :param key_value: Cadena que indica la contraseña de la clave de acceso (Access Key Password).
    :return: Cadena con los datos del token de acceso.
    """

    # Construir la URL de autoridad utilizando el identificador del Tenant de Azure
    authority_url = 'https://login.microsoftonline.com/' + tenant_id

    # Crear una instancia de AuthenticationContext con la URL de autoridad
    context = adal.AuthenticationContext(authority_url)

    # Obtener el token de acceso utilizando claves de cliente
    token = context.acquire_token_with_client_credentials(
        resource='https://management.azure.com/',
        client_id=client_id,
        client_secret=key_value
    )

    # Devolver la cadena de acceso del token
    return token["accessToken"]



def get_token_from_json( json_file ):
    """
    Login en la API de Azure Defender for Cloud para empezar a hacer querys, usando un fichero JSON como parámetro.

    :param json_file: Fichero JSON del que obtendremos los datos del TentantID y las access keys para conectar
    :return: String con los datos del token de acceso
    """

    f = open(json_file)
    data = json.load(f)
    token = get_token(data['TENANT_ID'], data['CLIENT_ID'], data['KEY_VALUE'])
    return token




def get_subscriptions(token, projects, as_dataframe=False):
    """
    Obtiene un listado de las subcripciones del Tenant de Azure.

    API docs: https://learn.microsoft.com/en-us/rest/api/resources/subscriptions/list?tabs=HTTP

    :param token: Cadena con los datos del token de acceso.
    :param projects: Dataframe con información de account groups y subscripciones.
    :param as_dataframe: True si queremos el resultado como dataframe, False en caso contrario (lista).
    :return: Dataframe/lista (según se elija) con los IDs de las suscripciones del Tenant.
    """

    # URL de la API para obtener la lista de suscripciones
    url = "https://management.azure.com/subscriptions?api-version=2020-01-01"

    # Realizar la llamada a la API utilizando el token de acceso y el método GET
    response_raw = paux.call_api(token, "GET", url)

    all_subs = pd.DataFrame(response_raw['value'])

    def extract_environment(tags):
        if pd.notna(tags) and 'Environment' in tags:
            return tags['Environment']
        else:
            return None

    all_subs['environment'] = all_subs['tags'].apply(extract_environment)

    all_subs.to_excel("all_subs.xlsx")

    # Inicializar una lista para almacenar las suscripciones
    subscriptions = []



    # Iterar sobre las respuestas de la API
    for s in response_raw['value']:
        if s['state'] == 'Enabled':
            sub = s.copy()
            sub['project'] = None
            try:
                sub['environment'] = sub['tags']['Environment']
            except:
                sub['environment'] = None

            # Iterar sobre los proyectos en el dataframe y asignar el proyecto a la suscripción
            for ag in projects['Proyecto'].drop_duplicates():
                if (
                    s['subscriptionId'] in list(projects[projects['Proyecto'] == ag]['subscriptionId'])
                    or s['displayName'] in list(projects[projects['Proyecto'] == ag]['Subscription'])
                ):
                    sub['project'] = ag


                    if (
                        not s['subscriptionId'] in list(projects[projects['Proyecto'] == ag]['subscriptionId'])
                        and s['displayName'] in list(projects[projects['Proyecto'] == ag]['Subscription'])
                    ):
                        print(s['subscriptionId'] + " -- " + s['displayName'])

            # Agregar la suscripción a la lista si tiene un proyecto asignado
            if sub['project'] is not None:
                subscriptions.append(sub)
            else:
                print(s['displayName'] + " no tiene responsable asignado")

    # Devolver la lista o el dataframe según la opción especificada
    if not as_dataframe:
        return subscriptions
    else:
        return pd.DataFrame.from_dict(subscriptions)





def get_secure_score_control_definitions(token, as_dataframe=False):
    """
    Obtiene un listado de los controles de seguridad disponibles, incluyendo descripción, puntuación máxima y políticas/assessments asociadas.

    API docs: https://learn.microsoft.com/en-gb/rest/api/defenderforcloud/secure-score-control-definitions/list?tabs=HTTP

    :param token: Cadena con los datos del token de acceso.
    :param as_dataframe: True si queremos el resultado como dataframe, False en caso contrario (lista).
    :return: Dataframe/lista (según se elija) con la información de los controles (ID, nombre, descripción, maxScore, IDs de políticas asociadas, etc).
    """

    # URL de la API para obtener la lista de definiciones de controles de seguridad
    url = "https://management.azure.com/providers/Microsoft.Security/secureScoreControlDefinitions?api-version=2020-01-01"

    # Realizar la llamada a la API utilizando el token de acceso y el método GET
    response_raw = paux.call_api(token, "GET", url)

    # Inicializar una lista para almacenar la información de los controles de seguridad
    sec = []

    # Iterar sobre las respuestas de la API
    for s in response_raw['value']:
        sec.append(s['properties'])

    # Devolver la lista o el dataframe según la opción especificada
    if not as_dataframe:
        return sec
    else:
        return pd.DataFrame.from_dict(sec)




def get_secure_score_controls(token, subscription_id, as_dataframe=False):
    """
    Obtiene un listado de los controles de seguridad de una subscripción, incluyendo nombre del control,
    recuento de estado de recursos que pasan/no pasan por sección, y puntuación/porcentaje.

    API docs: https://learn.microsoft.com/en-us/rest/api/defenderforcloud/secure-score-controls/list?tabs=HTTP

    :param token: Cadena con los datos del token de acceso.
    :param subscription_id: Cadena con el ID de la subscripción de Azure a evaluar.
    :param as_dataframe: True si queremos el resultado como dataframe, False en caso contrario (lista).
    :return: Dataframe/lista (según se elija) con el listado de recomendaciones/políticas, recuento de estado de recursos y puntuación.
    """

    # URL de la API para obtener la lista de controles de seguridad de una subscripción
    url = f"https://management.azure.com/subscriptions/{subscription_id}/providers/Microsoft.Security/secureScores/ascScore/secureScoreControls?api-version=2020-01-01&$expand=definition"

    # Realizar la llamada a la API utilizando el token de acceso y el método GET
    response_raw = paux.call_api(token, "GET", url)

    # Inicializar una lista para almacenar la información de los controles de seguridad
    sec = []

    # Iterar sobre las respuestas de la API
    for s in response_raw['value']:
        sec.append(s['properties'])

    # Devolver la lista o el dataframe según la opción especificada
    if not as_dataframe:
        return sec
    else:
        return pd.DataFrame.from_dict(sec)



def get_secure_score(token, subscription_id, secure_score_name ="ascScore", as_dataframe = False):
    """
    Listado con la puntuación de seguridad de una subscripción.
    La iniciativa por defecto usada es: "ascScore".
    API docs: https://learn.microsoft.com/en-us/rest/api/defenderforcloud/secure-scores/get?tabs=HTTP

    :param token: String con los datos del token de acceso
    :param subscription_id: String con el ID de la subscripción de Azure a evaluar
    :param secure_score_name: String con la iniciativa. Por defecto, se usa "ascScore"
    :param as_dataframe: True si queremos el resultado como dataframe, False en caso contrario (lista)
    :return: dataframe/lista (según se elija) con el resultado de la evaluación de la seguridad
    """

    url = "https://management.azure.com/subscriptions/" + subscription_id + "/providers/Microsoft.Security/secureScores/" + secure_score_name + "?api-version=2020-01-01"
    response_raw = paux.call_api(token, "GET", url)

    sec = []
    for s in response_raw['value']:
        sec.append(s['properties'])

    if (not as_dataframe):
        return sec
    else:
        return pd.DataFrame.from_dict(sec)


def get_assessment_metadata( token, assessment_id ):
    """
    Obtiene información en base al ID de una política de seguridad. como nombre, descripción, severidad, categoría, etc).
    API docs: https://learn.microsoft.com/en-us/rest/api/defenderforcloud/assessments-metadata/get?tabs=HTTP

    :param token: String con los datos del token de acceso
    :param assessment_id: String con el ID de la política de seguridad
    :return: JSON con información de la política (ID, nombre, tipo, descripción, remediación, categoría, severidad, impacto, etc)
    """

    url = "https://management.azure.com/providers/Microsoft.Security/assessmentMetadata/" + assessment_id + "?api-version=2020-01-01"
    response_raw = paux.call_api(token, "GET", url)

    return response_raw

def get_assessments( token, subscription_id, as_dataframe = False ):
    """
    Obtiene un listado de evaluaciones de una subscripción incluyendo la política/assessment, recurso, y estado (healthy o no)
    API docs: https://learn.microsoft.com/en-us/rest/api/defenderforcloud/assessments/list?tabs=HTTP

    :param token: String con los datos del token de acceso
    :param subscription_id: String con el ID de la subscripción de Azure a evaluar
    :param as_dataframe: True si queremos el resultado como dataframe, False en caso contrario (lista)
    :return: dataframe/lista (según se elija) con el listado de evaluaciones de seguridad (nombre política/assessment, recurso, y estado: healthy/unHealthy)
    """

    url = "https://management.azure.com/subscriptions/" + subscription_id + "/providers/Microsoft.Security/assessments?api-version=2020-01-01"
    response_raw = paux.call_api(token, "GET", url)



    sec = []
    if(response_raw['value'] == []):
        print("Account " + subscription_id + " doesnt have assessments")
    else:

        for s in response_raw['value']:
            ass = s['properties'].copy()
            ass['subscriptionId'] = subscription_id
            sec.append(ass)

    if (not as_dataframe):
        return sec
    else:
        return pd.DataFrame.from_dict(sec)


def get_connectors( token, subscription_id ):
    """
    Obtiene un listado con información de conectores de cuentas (tipo AWS, GCP, GitHub) asociados a una subscripción en Defender For Cloud
    API docs: https://learn.microsoft.com/en-us/rest/api/defenderforcloud/connectors/list?tabs=HTTP

    :param token: String con los datos del token de acceso
    :param subscription_id: String con el ID de la subscripción de Azure a evaluar
    :return: lista con información del conector (ID cuenta, nombre, roles/permisos, tipo autenticación, etc)
    """

    url = "https://management.azure.com/subscriptions/" + subscription_id + "/providers/Microsoft.Security/securityConnectors?api-version=2021-12-01-preview"
    response_raw = paux.call_api(token, "GET", url)
    return response_raw['value']


def get_aws_accounts( token, subscriptions, as_dataframe = False ):
    """
    Obtiene un listado con las cuentas de AWS asociadas a cada una de las subscripciones suministradas en Defender For Cloud.

    :param token: String con los datos del token de acceso
    :param subscriptions: Lista con los IDs de las subscripciones del Tenant de Azure
    :param as_dataframe: True si queremos el resultado como dataframe, False en caso contrario (lista)
    :return: dataframe/lista (según se elija) con información del conector (ID cuenta, nombre, roles/permisos, tipo autenticación, etc)
    """

    aws = []
    for sub in subscriptions:
        cons = get_connectors(token, sub)
        for con in cons:
            conname = con['name']
            accountid = con['properties']['hierarchyIdentifier']
            aws.append({"connectorName":conname, "accountId":accountid})

    if(not as_dataframe):
        return aws
    else:
        return pd.DataFrame.from_dict(aws)



class SecureScoreControls:
    def __init__(self, token, projects, client_name, recommendations, only_unhealthy = True):
        """
        Inicializa la clase SecureScoreControls.

        :param self: Objeto para representar la instancia de la clase SecureScoreControls
        :param token: String con los datos del token de acceso
        :param projects: Dataframe con información de los account groups
        :param client_name: String con el nombre del cliente
        :param recommendations: Lista con los nombres de recomendaciones/políticas
        """


        self.token = token
        self.projects = projects
        self.recommendations = recommendations

        self.only_unhealthy = only_unhealthy



        if(self.recommendations.empty):
            self.all_recommendations = True
        else:
            self.all_recommendations = False

        self.subscriptions = get_subscriptions(token, projects=projects, as_dataframe=True)

        self.tenantID = self.subscriptions['tenantId'][0]
        self.client_name = client_name
        self.subscriptions = self.subscriptions[['subscriptionId', 'displayName', 'state', 'project', 'environment']]
        self.subscriptions.rename(columns={"displayName":"subscriptionName"}, inplace=True)
        self.subscriptions.to_excel("subscriptions.xlsx")

        #self.aws_accounts = get_aws_accounts(token, self.subscriptions['subscriptionId'], as_dataframe=True)
        self.aws_accounts = []

        # Carga los nombres e IDs de las recomendaciones
        self.load_scc()
        # Carga los datos de las recomendaciones, como descripción y remediación
        self.load_assessments_metadata()
        # Une los dos dataframes anteriores
        self.merge_scc_and_metadata()
        # Cargo los fallos de cada suscripción. De aquí puedo sacar % de cumplimiento de cada recomendación.
        self.load_assessments()
        # Une los fallos de cada suscripción con la info de cada recomendación
        self.merge_scc_and_assessments()
        # Obtiene scores
        self.get_scores()
        # Añade las labels de nuestras recomendaciones
        self.add_labels()
        # Generamos hashes únicos para identificar cada 'alerta'
        self.add_hashes()

        self.export()


    def load_scc(self):
        """
        Obtiene los datos de los controles de seguridad (requirements/sections), como:
        ID, nombre, descripción, maxScore, IDs de políticas asociadas, etc.

        :param self: Objeto para representar la instancia de la clase SecureScoreControls
        """

        self.scc = get_secure_score_control_definitions(self.token, as_dataframe=True)[['displayName', 'assessmentDefinitions']].explode('assessmentDefinitions')
        self.scc['assessmentDefinitions'] = self.scc['assessmentDefinitions'].apply(lambda x: x['id'].split("assessmentMetadata/")[1])

    def load_assessments_metadata(self):
        """
        Obtiene información detallada de los assessments/políticas de seguridad
        (ID, nombre, tipo, descripción, remediación, categoría, severidad, impacto, etc).

        :param self: Objeto para representar la instancia de la clase SecureScoreControls.
        """

        # Obtener los IDs de los assessments/políticas desde la instancia de SecureScoreControls
        metadata_ids = list(self.scc['assessmentDefinitions'])
        metadata_info = []  # Lista para almacenar la información detallada de los assessments seleccionados
        all_metadata = []  # Lista para almacenar la información de todos los assessments, independientemente de si están seleccionados o no
        errors = 0
        i = 0

        # Iterar sobre los IDs de los assessments
        for id in metadata_ids:
            i += 1
            if i % 200 == 0:
                print("Loading " + str(i) + "/" + str(len(metadata_ids)) + " with " + str(errors) + " errors ")

            # Obtener información detallada de un assessment
            metadata = get_assessment_metadata(self.token, assessment_id=id)

            # Verificar si hay errores en la respuesta de la API
            if 'Error' not in metadata.keys():
                metadata['properties']['assessmentDefinitionId'] = id
                metadata['properties']['description'] = BeautifulSoup(metadata['properties']['description'], "html.parser").get_text()
                metadata['properties']['remediationDescription'] = BeautifulSoup(metadata['properties']['remediationDescription'],"html.parser").get_text()

                # Verificar si se deben incluir todas las recomendaciones o solo las específicas
                pol_list = self.recommendations['Policy'].to_list()
                if self.all_recommendations or metadata['properties']['displayName'] in pol_list:
                    metadata_info.append(metadata['properties'])
                    metin = metadata['properties'].copy()
                    metin['Selected'] = True
                else:
                    metin = metadata['properties'].copy()
                    metin['Selected'] = False

                all_metadata.append(metin)
            else:
                errors += 1
                print("Error with metadata of " + str(metadata))

        print(str(errors) + " errors loading metadata info")

        # Crear un DataFrame con la información detallada de los assessments seleccionados
        self.metadata = pd.DataFrame(metadata_info)

        # Combinar la información de todos los assessments con las etiquetas (labels)
        todas = pd.DataFrame(all_metadata).merge(self.recommendations, left_on='displayName', right_on='Policy',
                                                 how='left')

        # Eliminar duplicados basados en la columna 'description'
        todas = todas.drop_duplicates(subset=['description'])


    def merge_scc_and_metadata(self):
        """
        Une los datos de los controles de seguridad (requirements/sections) con los de assessments/políticas de seguridad (información detallada).

        :param self: Objeto para representar la instancia de la clase SecureScoreControls
        """
        self.scc_with_meta = self.scc.merge(self.metadata, left_on="assessmentDefinitions", right_on="assessmentDefinitionId", how="right")



        self.scc_with_meta.rename(columns={'displayName_x': 'sccDisplayName', 'displayName_y': 'assessmentDisplayName'}, inplace=True)


    def load_assessments(self):
        """
        Obtiene información detallada de los assessments/políticas de seguridad asociadas a una subscripción
        (nombre política/assessment, recurso, y estado: healthy/unHealthy).

        :param self: Objeto para representar la instancia de la clase SecureScoreControls.
        """

        all_assessments = []  # Lista para almacenar información detallada de todos los assessments de todas las subscripciones
        count = 1

        # Iterar sobre las subscripciones y obtener assessments asociados a cada una
        for sub in self.subscriptions['subscriptionId']:
            ass = get_assessments(self.token, sub)
            for a in ass:
                try:
                    a['resourceId'] = a['resourceDetails']['Id']
                except:
                    a['resourceId'] = None


            all_assessments += ass.copy()

            print("Getting assessments: " + str(count) + "/" + str(len(self.subscriptions['subscriptionId'])) + '\r')
            count += 1

        assessments = []

        # Filtrar assessments que tienen estado 'Unhealthy'
        for a in all_assessments:
            if a['status']['code'] == 'Unhealthy' or not self.only_unhealthy:
                assessments.append(a)

        # Crear un DataFrame con la información de assessments con estado 'Unhealthy'
        self.assessments = pd.DataFrame(assessments)

        # Combinar la información de assessments con la información de las subscripciones
        self.assessments = self.assessments.merge(self.subscriptions, left_on="subscriptionId",
                                                  right_on="subscriptionId", how="inner")

        # Añadir una columna 'Cloud' con el valor 'Azure'
        self.assessments['Cloud'] = 'Azure'

    def merge_scc_and_assessments(self):
        """
        Une los datos de los controles de seguridad (requirements/sections) con los de assessments/políticas de seguridad (información básica).

        :param self: Objeto para representar la instancia de la clase SecureScoreControls
        """

        self.scc_with_assessments = self.scc_with_meta.merge(self.assessments, left_on="assessmentDisplayName", right_on="displayName", how='left')


    def getcode(self, x):
        try:
            return x['code']
        except:
            return None

    def get_scores(self):
        """
        Calculamos scores
        """
        try:
            # Intentar calcular el código de estado para la columna 'status' en la instancia de SecureScoreControls
            self.scc_with_assessments['statusCode'] = self.scc_with_assessments['status'].apply(
                lambda x: self.getcode(x))
        except:
            print(444)

        # Inicializar un diccionario para almacenar los scores
        self.scores = {'subscriptionID': [], 'healthy': [], 'unhealthy': [], 'total': [], 'score': []}

        # Iterar sobre las subscripciones
        for sub in self.subscriptions['subscriptionId']:
            tmp = self.scc_with_assessments[self.scc_with_assessments['subscriptionId'] == sub].copy()

            # Convertir columnas a cadenas para evitar problemas al guardar en Excel
            tmp['resourceId'] = tmp['resourceId'].apply(lambda x: str(x))
            tmp['resourceDetails'] = tmp['resourceDetails'].apply(lambda x: str(x))
            tmp['categories'] = tmp['categories'].apply(lambda x: str(x))
            tmp['threats'] = tmp['threats'].apply(lambda x: str(x))
            tmp['additionalData'] = tmp['additionalData'].apply(lambda x: str(x))

            try:
                tmp['status'] = tmp['status'].apply(lambda x: str(x))
            except:
                pass

            tmp.drop_duplicates(inplace=True)


            # Calcular la cantidad de controles saludables y no saludables
            healthy = tmp[tmp['statusCode'] == 'Healthy'].shape[0]
            unhealthy = tmp[tmp['statusCode'] == 'Unhealthy'].shape[0]

            # Calcular el score en base a los controles saludables y no saludables
            if (healthy + unhealthy == 0):
                scorenum = None
            else:
                scorenum = int(100 * healthy / (healthy + unhealthy))

            # Agregar la información al diccionario de scores
            self.scores['subscriptionID'].append(sub)
            self.scores['healthy'].append(healthy)
            self.scores['unhealthy'].append(unhealthy)
            self.scores['total'].append(healthy + unhealthy)
            self.scores['score'].append(scorenum)

        # Crear un DataFrame con la información de scores
        scoresdf = pd.DataFrame(self.scores)

        # Combinar la información de scores con la información de subscripciones
        scoresdf = scoresdf.merge(self.subscriptions, left_on='subscriptionID', right_on='subscriptionId', how='left')

        # Guardar la información de scores en un archivo Excel
        scoresdf.to_excel("ScoresBySub.xlsx")

    def add_labels(self):

        self.scc_with_assessments = self.scc_with_assessments.merge(self.recommendations, left_on="assessmentDisplayName", right_on="Policy", how='left')
        #self.scc_with_assessments.drop(['Policy'], inplace=True)


    def hash_values(self, row):
        combined_string = str(row['sccDisplayName']) + str(row['displayName']) + str(row['resourceId'])
        return hashlib.sha256(combined_string.encode()).hexdigest()

    def add_hashes(self):
        self.scc_with_assessments['hash'] = self.scc_with_assessments.apply(self.hash_values, axis=1)



    def export(self):
        """
        Exporta la información de controles de seguridad (requirements/sections) y de políticas/assessments en Excel.

        :param self: Objeto para representar la instancia de la clase SecureScoreControls.
        """

        # Guardar la información de controles de seguridad y assessments en un archivo Excel

        column_name_mapping = {
            "sccDisplayName": "recommendationCategory",
            "assessmentDisplayName": "recommendation",
            "project": "owner",
            "label": "xtratusLabel",
            "hash": "hashIdentifier"
        }

        # Renombra las columnas según el mapeo
        tmp = self.scc_with_assessments.copy()
        # Renombra las columnas según el mapeo
        tmp.columns = [column_name_mapping.get(col, col) for col in tmp.columns]



        tmp['secondaryOwner'] = ""

        #tmp['managementNotes'] = ""

        tmp.drop(['status'], axis=1, inplace=True)
        tmp.rename(columns={"statusCode":"status"}, inplace=True)
        tmp['scanDate'] = datetime.date.today().strftime("%d/%m/%Y")

        tmp.drop_duplicates(subset=['hashIdentifier'], inplace=True)

        tmp.to_excel("output_" + self.client_name + ".xlsx", index=False)

        # Inicializar variables para el manejo del archivo histórico
        first = False
        filename = "historic_" + self.client_name + ".xlsx"

        # Verificar si el archivo histórico ya existe
        if not os.path.isfile(filename):
            first = True
            wb = openpyxl.Workbook()
            wb.save(filename)

        # Configurar el escritor de Excel para añadir datos al archivo histórico
        writer = pd.ExcelWriter(filename, engine='openpyxl', mode='a', if_sheet_exists='overlay')

        # Obtener la fecha actual en formato "dd/mm/yyyy"
        date = datetime.date.today().strftime(format="%d/%m/%Y")

        # Realizar un conteo de controles de seguridad por severidad, suscripción y proyecto
        counts = self.scc_with_assessments.groupby(['project', 'subscriptionId', 'severity']).size().reset_index(
            name='counts')

        # Filtrar conteos por severidad
        highs = counts[counts['severity'] == 'High'].copy()
        highs.rename(columns={"counts": "High"}, inplace=True)
        mediums = counts[counts['severity'] == 'Medium'].copy()
        mediums.rename(columns={"counts": "Medium"}, inplace=True)
        lows = counts[counts['severity'] == 'Low'].copy()
        lows.rename(columns={"counts": "Low"}, inplace=True)

        # Combinar los conteos por severidad
        result = highs.merge(mediums, how="outer", left_on="subscriptionId", right_on="subscriptionId")
        result = result.merge(lows, how="outer", left_on="subscriptionId", right_on="subscriptionId")
        result = result.merge(self.subscriptions[['subscriptionId', 'subscriptionName']], how="left",
                              left_on="subscriptionId", right_on="subscriptionId")
        result.reset_index()
        result.drop(['severity', 'project_x', 'project_y', 'severity_x', 'severity_y'], axis=1, inplace=True)
        result.reset_index()

        # Añadir la fecha actual a la información
        result['date'] = date
        print(result)

        # Guardar la información en el archivo histórico
        if first:
            result.to_excel(writer, sheet_name='Sheet', header=True, index=False)
        else:
            result.to_excel(writer, sheet_name='Sheet', startrow=writer.sheets['Sheet'].max_row, header=None,
                            index=False)
        writer.close()


