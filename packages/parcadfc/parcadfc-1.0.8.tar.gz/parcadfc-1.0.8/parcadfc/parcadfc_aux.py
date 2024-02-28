import parcadfc
import requests
import json
import datetime
import os
from shutil import copyfile
from docxtpl import DocxTemplate
import pandas as pd
from docxcompose.composer import Composer
import shutil

from os.path import isfile, join
import os

from importlib import resources

#import win32com.client

#from docx2pdf import convert



def call_api( token, method, endpoint ):
    """
    Listado con la puntuación de seguridad de una subscripción

    :param token: String con los datos del token de acceso
    :param method: String con el tipo de método HTTP a usar: GET, POST, etc
    :param endpoint: String con la URL del recurso
    :return: json con el resultado de la evaluación de la seguridad
    """

    headers = {
        'Content-Type': 'application/json',
        'Authorization': "Bearer " + token
    }

    result = requests.request(method, endpoint, headers=headers)
    result = json.loads(result.text)
    return result


def get_projects(filename):
    """
    Obtiene proyectos (Account Groups) desde un fichero Excel suministrado

    :param filename: String con la ruta/nombre del fichero Excel
    :return: Dataframe con la información del Excel
    """

    return pd.read_excel(filename)


def get_recommendations(xlsxpath):
    """
    Obtiene las recomendaciones de seguridad desde un fichero XLSX suministrado.

    :param xlsxpath: String con la ruta/nombre del fichero JSON
    :return: Diccionario con la información del JSON
    """

    df = pd.read_excel(xlsxpath)
    return df


def clean_characters(string):
    """
    Reemplaza los caracteres "<>" por "_" de un String suministrado para facilitar la legibilidad

    :param string: String con la cadena de texto a limpiar
    :return: String con la cadena de texto reemplazada
    """

    chars = ['<','>']
    clean = string
    for c in chars:
        try:
            clean = clean.replace(c,"_")
        except:
            pass

    return clean


def docx_to_pdf(path):
    """
    Pendiente

    :param path: String con la ruta del documento de Word
    :return: Documento convertido en PDF
    """

    pass




class MakeReport:
    def __init__(self, scc, where_to_create_path, logo_path):
        """
        Inicializa la clase MakeReport

        :param self: Objeto para representar la instancia de la clase MakeReport
        :param scc: String con la iniciativa (secure_score_control)
        :param logo_path: String con el path del logo para los informes
        :param pdf: Boolean para indicar si es PDF. Por defecto, False
        """

        self.logo_path = logo_path
        # Asigna el valor de scc al atributo de la instancia
        self.scc = scc
        self.scc.scc_with_assessments = self.scc.scc_with_assessments[self.scc.scc_with_assessments['statusCode'] == 'Unhealthy']
        self.scc.scc_with_assessments = self.scc.scc_with_assessments[self.scc.scc_with_assessments['remediationTeam'] != 'Xtratus']

        # Configura algunos atributos basados en la iniciativa (scc) proporcionada
        self.labels = scc.recommendations

        # Obtiene la ruta del directorio actual del archivo en ejecución
        self.creation_path = where_to_create_path


        # Define las rutas de los directorios para plantillas y creación de informes
        self.template_path = str(resources.files('parcadfc') / 'paux_material')
        self.making_path = self.creation_path + "/making_report"

        # Crea el directorio 'reports' si no existe
        if not os.path.exists(self.creation_path + "/reports/"):
            os.makedirs(self.creation_path + "/reports/")

        # Elimina y recrea el directorio 'making_report'
        if os.path.exists(self.making_path):
            shutil.rmtree(self.making_path)
        os.makedirs(self.making_path)

        # Llama al método makeExcel para realizar alguna inicialización relacionada con Excel
        self.makeExcel()

        # Itera sobre proyectos únicos en la iniciativa scc
        for ag in self.scc.projects['Proyecto'].drop_duplicates():
            # Asigna el nombre del proyecto actual
            self.project = ag
            if ag == False:
                self.project = "None"

            # Obtiene el número de vulnerabilidades en el proyecto actual
            num_vuln = len(self.scc.scc_with_assessments[self.scc.scc_with_assessments['project'] == self.project])

            # Si hay al menos una vulnerabilidad, genera un informe y un archivo Excel
            if num_vuln > 0:
                self.makeReport()
                self.makeExcel(self.project)
            else:
                # Si no hay vulnerabilidades, imprime un mensaje indicando esto
                print(str(self.project) + " tiene 0 vulnerabilidades")

        # Elimina el directorio 'making_report' después de completar el proceso
        shutil.rmtree(self.making_path)

    def makeExcel(self, project=None):
        """
        Genera un fichero Excel en la carpeta /reports, en base al proyecto suministrado. Si no es así, reporta todas las suscripciones

        :param self: Objeto para representar la instancia de la clase MakeReport
        :param project: String con el nombre del proyecto. Por defecto, no es necesario (en este caso, reporta todas las suscripciones)
        """
        # Mapea los nombres de columna a nombres más descriptivos


        # Verifica si se proporciona un nombre de proyecto
        if project is None:
            # Si no se proporciona un proyecto, crea un informe para todas las suscripciones
            self.scc.scc_with_assessments.to_excel(
                self.creation_path + "/reports/" + "Report_all_subscriptions_" + str((datetime.date.today()).strftime("%d-%m-%Y")) + ".xlsx",
                index=False
            )
        else:
            # Si se proporciona un proyecto, filtra las evaluaciones correspondientes a ese proyecto
            tmp = self.scc.scc_with_assessments[self.scc.scc_with_assessments['project'] == self.project]
            column_name_mapping = {
                "sccDisplayName": "recommendationCategory",
                "assessmentDisplayName": "recommendation",
                "project": "owner",
                "label": "xtratusLabel",
                "hash": "hashIdentifier"
            }


            # Renombra las columnas según el mapeo
            tmp.columns = [column_name_mapping.get(col, col) for col in
                           self.scc.scc_with_assessments.columns]
            # Selecciona columnas específicas para el informe
            tmp = tmp[[
                "severity", "subscriptionName", "owner", "recommendation", "description", "remediationDescription",
                "resourceId", "userImpact", "implementationEffort", "statusCode"
            ]]


            # Crea un informe Excel específico para el proyecto y la fecha actual
            tmp.to_excel(
                self.creation_path + "/reports/" + "Report_" + self.project + "_" + str((datetime.date.today()).strftime("%d-%m-%Y")) + ".xlsx",
                index=False
            )


    def makeReport(self):
        """
        Genera un informe con portada, recomendaciones.

        :param self: Objeto para representar la instancia de la clase MakeReport
        """

        self.makeReportCover()
        self.makeReportRecommendations()
        self.compose()

    def makeReportCover(self):
        """
        Genera la portada del informe en formato Word, en base a una plantilla existente, con los datos del cliente

        :param self: Objeto para representar la instancia de la clase MakeReport
        """

        # Copia la plantilla de la portada a un archivo temporal en la carpeta de creación de informes
        copyfile(self.template_path + '/templateCover.docx', self.making_path + '/cover_temp.docx')

        # Carga la plantilla del archivo temporal
        doc = DocxTemplate(self.making_path + '/cover_temp.docx')

        # Define el contexto con los datos del cliente y del proyecto
        context = {'ag': self.project,
                   'client_name': self.scc.client_name,
                   'date': str((datetime.date.today()).strftime("%d-%m-%Y")),
                   'title1': "Reporte de Defender for Cloud",
                   'title2': " Owner: "
                   }

        # Agrega información de suscripciones al contexto
        context['subscription'] = '\n\r'
        subs = self.scc.subscriptions[self.scc.subscriptions['project'] == self.project]
        for s in subs['subscriptionName']:
            context['subscription'] += s + '\n\r'

        # Reemplaza la imagen del logo en la plantilla con el logo específico del cliente
        doc.replace_pic('logo.png', self.logo_path)

        # Renderiza la plantilla con el contexto proporcionado
        doc.render(context)

        # Guarda el resultado en un nuevo archivo de salida
        doc.save(self.making_path + '/cover_output.docx')

        # Elimina el archivo temporal
        os.remove(self.making_path + '/cover_temp.docx')


    def initialize(self):
        """
        Inicializa el objeto de la clase MakeReport con los datos de los proyectos de la suscripción

        :param self: Objeto para representar la instancia de la clase MakeReport
        """

        self.subscriptions = self.scc.subscriptions[self.scc.subscriptions['project'] == self.project]
        self.scc_with_assessments = self.scc.scc_with_assessments[self.scc.scc_with_assessments['project'] == self.project]
        self.rec_index = 0
        

    def makeReportRecommendationPage(self, recommendation):
        """
        Genera la página del informe en formato Word, con los datos de las recomendaciones de los controles de seguridad,
        en base a una plantilla existente y los datos del cliente

        :param self: Objeto para representar la instancia de la clase MakeReport
        :param recommendation: String con la recomendación de seguridad
        """

        # Incrementa el índice de recomendación
        self.rec_index += 1
        first = True
        resources = []

        # Itera sobre las recomendaciones y recopila información
        for index, row in recommendation.iterrows():
            resources.append({"resource": row['resourceDetails'], "hash": row['hash'], "subName": row['subscriptionName']})
            if(first):
                first = False
                rec_cat = row['sccDisplayName']
                rec = row['displayName']
                ui = row['userImpact']
                ie = row['implementationEffort']
                sev = row['severity']
                afn = str(recommendation.shape[0])
                desc = row['description']
                rem = row['remediationDescription']
                coste = row['remediationCost']

                context = {
                    "afn": str(afn),
                    "rc": rec_cat,
                    "sev": sev,
                    "ui": ui,
                    "ie": ie,
                    "recdesc": desc,
                    "remediation": rem,
                    "recommendation_name": rec,
                    "coste": coste
                }

            context['label_optional'] = "Politica XTRATUS:"
            context['label_value'] = row['xtratusLabel']

        # Limpia los caracteres en el contexto
        for key in context:
            context[key] = clean_characters(context[key])

        # Copia la plantilla de recomendación a un archivo temporal en la carpeta de creación de informes
        copyfile(self.template_path + '/templateRec.docx', self.making_path + '/template_' + str(self.rec_index) + '_temp.docx')
        doc = DocxTemplate(self.making_path + '/template_' + str(self.rec_index) + '_temp.docx')

        # Reemplaza la imagen del nivel de severidad en la plantilla con la imagen correspondiente
        doc.replace_pic('Picture 4', self.template_path + '/images/' + sev.lower())

        affected_resources = []
        for ar in resources:
            sub_name = ar['subName']
            res_name = ar['resource']

            try:
                res_name = ar['resource']['Id']
            except:
                res_name = ar['resource']['MachineName']

            hash = ar['hash']

            affected_resources.append({'resourceName': res_name, 'hash': hash, 'subscription': sub_name})

        context['resource_list'] = affected_resources
        context['afn'] = str(len(affected_resources))

        # Renderiza la plantilla con el contexto proporcionado
        self.empty_index = []
        if len(affected_resources) >= 0:
            doc.render(context)
            doc.save(self.making_path + '/template_' + str(self.rec_index) + '_output.docx')
            os.remove(self.making_path + '/template_' + str(self.rec_index) + '_temp.docx')
        else:
            self.empty_index.append(self.rec_index)
            os.remove(self.making_path + '/template_' + str(self.rec_index) + '_temp.docx')

        # Imprime información sobre el progreso del informe
        try:
            print(self.project + ": Completed: " + rec_cat + ": " + rec + " (" + str(self.rec_index) + "/" + str(self.total_recs) + ")\r")
        except:
            print(self.project)
            print(rec_cat)
            print(rec)


    def makeReportRecommendations(self):
        """
        Genera el cuerpo del informe con todas las recomendaciones de los controles de seguridad en formato Word, 
        en base a una plantilla existente, con los datos del cliente

        :param self: Objeto para representar la instancia de la clase MakeReport
        """

        self.initialize()
        recs = self.scc_with_assessments['displayName'].drop_duplicates()
        self.total_recs = len(recs)

        """
        label_value = None

        try:
            label_name = self.label_name
        except:
            label_name = None
        """

        i = 0
        for rec in recs:
            #if(label_name != None):
                #label_value = self.labels['values'][i]
            self.makeReportRecommendationPage(self.scc_with_assessments[self.scc_with_assessments['displayName'] == rec])
            i += 1
        


    def compose(self):
        """
        Compone informe final (portada y cuerpo) con todas las recomendaciones de los controles de seguridad
        Se genera como Word por defecto. Si se hubiera activado la opción de PDF, se convierte a este formato

        :param self: Objeto para representar la instancia de la clase MakeReport
        """

        try:
            # Copia la portada generada a un archivo temporal
            copyfile(self.making_path + '/cover_output.docx', self.making_path + '/cover_output_tmp.docx')

            # Carga la plantilla de la portada temporal
            doc = DocxTemplate(self.making_path + "/cover_output_tmp.docx")
            self.composer = Composer(doc)

            # Itera sobre las recomendaciones generadas y agrega sus informes al informe final
            for i in range(1, self.rec_index + 1):
                if i not in self.empty_index:
                    doc = DocxTemplate(self.making_path + "/template_" + str(i) + "_output.docx")
                    self.composer.append(doc)

            # Guarda el informe final en un archivo Word
            docpath = self.creation_path + "/reports/" + "Report_" + self.project + "_" + str((datetime.date.today()).strftime("%d-%m-%Y")) + ".docx"
            self.composer.save(docpath)

        except Exception as e:
            # Captura y maneja cualquier error durante el proceso
            print("Error con informe " + self.project)
            print(str(e))



def ToCandPDF(path):
    """
    Actualiza los índices de tabla de contenido en archivos .docx y luego los convierte a archivos .pdf.

    :param path: Ruta del directorio que contiene los archivos .docx a procesar
    """

    import win32com.client
    from docx2pdf import convert

    def __updateIndex(filename):
        # Función interna para actualizar el índice de tabla de contenido en un archivo .docx
        word = win32com.client.DispatchEx("Word.Application")
        print("Updating ToC of: " + filename)
        doc = word.Documents.Open(os.path.join(os.path.dirname(os.path.abspath(__file__)) + path, filename))
        doc.TablesOfContents(1).Update()
        doc.Close(SaveChanges=True)
        word.Quit()

    # Obtiene la lista de archivos en el directorio
    files = [f for f in os.listdir(os.path.dirname(os.path.abspath(__file__)) + path) if
             isfile(join(os.path.dirname(os.path.abspath(__file__)) + path, f))]

    # Itera sobre los archivos en el directorio
    for f in files:
        if f[-5:] == ".docx":
            # Actualiza el índice de tabla de contenido para archivos .docx
            __updateIndex(f)

    # Convierte todos los archivos .docx en el directorio a archivos .pdf
    convert(os.path.join(os.path.dirname(os.path.abspath(__file__)) + path))






