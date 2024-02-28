from .cfdi_requests import make_request
from .endpoints import Endpoints


class FacturaComClient:
    def __init__(self, api_key, secret_key, url="https://sandbox.factura.com/api/v4"):
        """
        Inicializa un cliente para interactuar con la API de Factura.com.

        Args:
            api_key (str): La clave de la API.
            secret_key (str): La clave secreta de la API.
            url (str, opcional): La URL base de la API. Por defecto, es la URL de sandbox.

        Returns:
            None
        """
        self.api_key = api_key
        self.secret_key = secret_key
        self.base_url = url.rstrip('/')
        self.endpoints = Endpoints(self.base_url)
        self.headers = {
            "Content-Type": "application/json",
            "F-PLUGIN": "9d4095c8f7ed5785cb14c0e3b033eeb8252416ed",
            "F-Api-Key": self.api_key,
            "F-Secret-Key": self.secret_key
        }

    def get_invoice_list(self, **params):
        """
        Obtiene una lista de facturas según los parámetros proporcionados.

        Args:
            **params: Parámetros opcionales que se pueden proporcionar para filtrar la lista de facturas.
                month (int, opcional): El número de mes que deseas consultar (por ejemplo, 01 para enero).
                year (int, opcional): El año que deseas consultar (por ejemplo, 2024).
                rfc (str, opcional): El RFC para filtrar las facturas.
                type_document (str, opcional): El tipo de CFDI para listar solo las facturas de ese tipo.
                page (int, opcional): El número de página a consultar. Por defecto, es la página 1.
                per_page (int, opcional): El límite de resultados por página. Por defecto, retorna 100 registros.

        Returns:
            dict: Un diccionario que contiene la lista de facturas en formato JSON.

        Raises:
            requests.exceptions.RequestException: Si ocurre un error al realizar la solicitud HTTP.
        """
        return make_request(self.api_key, self.secret_key, self.base_url, 'GET', 'cfdi_list', params=params)

    def get_invoice_by_uid(self, cfdi_uid):
        """
        Obtiene una factura por su UID.

        Args:
            cfdi_uid (str): El UID de la factura que se desea obtener.

        Returns:
            dict: Un diccionario que contiene la información de la factura en formato JSON.

        Raises:
            requests.exceptions.RequestException: Si ocurre un error al realizar la solicitud HTTP.
        """
        return make_request(self.api_key, self.secret_key, self.base_url, 'GET', 'cfdi_uid',
                            params=cfdi_uid)

    def get_invoice_by_uuid(self, cfdi_uuid):
        """
        Obtiene una factura por su UUID.

        Args:
            cfdi_uuid (str): El UUID de la factura que se desea obtener.

        Returns:
            dict: Un diccionario que contiene la información de la factura en formato JSON.

        Raises:
            requests.exceptions.RequestException: Si ocurre un error al realizar la solicitud HTTP.
        """
        return make_request(self.api_key, self.secret_key, self.base_url, 'GET', 'cfdi_uuid',
                            params=cfdi_uuid)

    def get_invoice_by_folio(self, folio):
        """
        Obtiene una factura por su folio.

        Args:
            folio (str): El folio de la factura que se desea obtener.

        Returns:
            dict: Un diccionario que contiene la información de la factura en formato JSON.

        Raises:
            requests.exceptions.RequestException: Si ocurre un error al realizar la solicitud HTTP.
        """
        return make_request(self.api_key, self.secret_key, self.base_url, 'GET', 'cfdi_folio', params=folio)

    def create_invoice_4_0(self, invoice_data):
        """
        Crea una nueva factura.

        Args:
            invoice_data (dict): Los datos de la factura a crear.

        Returns:
            dict: Un diccionario que contiene la respuesta de la creación de la factura en formato JSON.

        Raises:
            requests.exceptions.RequestException: Si ocurre un error al realizar la solicitud HTTP.
        """
        return make_request(self.api_key, self.secret_key, self.base_url, 'POST', 'cfdi_create', data=invoice_data)

    def get_invoice_pdf(self, cfdi_uuid):
        """
        Obtiene el PDF de una factura por su UUID.

        Args:
            cfdi_uuid (str): El UUID de la factura de la cual se desea obtener el PDF.

        Returns:
            dict: Un diccionario que contiene el contenido del PDF en formato JSON.

        Raises:
            requests.exceptions.RequestException: Si ocurre un error al realizar la solicitud HTTP.
        """
        return make_request(self.api_key, self.secret_key, self.base_url, 'GET', 'cfdi_pdf',
                            params=cfdi_uuid)

    def get_invoice_xml(self, cfdi_uuid):
        """
        Obtiene el XML de una factura por su UUID.

        Args:
            cfdi_uuid (str): El UUID de la factura de la cual se desea obtener el XML.

        Returns:
            dict: Un diccionario que contiene el contenido del XML en formato JSON.

        Raises:
            requests.exceptions.RequestException: Si ocurre un error al realizar la solicitud HTTP.
        """
        data = {
            "cfdi_uuid": cfdi_uuid
        }
        return make_request(self.api_key, self.secret_key, self.base_url, 'GET', 'cfdi_xml',
                            params=cfdi_uuid)

    def cancel_invoice(self, cfdi_uuid, motivo, folio_sustituto):
        """
        Cancela una factura.

        Args:
            cfdi_uuid (str): El UUID de la factura que se desea cancelar.
            motivo (str): El motivo por el cual se solicita la cancelación del CFDI.
            folio_sustituto (str): El UID o UUID del CFDI que reemplazará al CFDI cancelado.

        Returns:
            dict: Un diccionario que contiene la respuesta de la cancelación de la factura en formato JSON.

        Raises:
            requests.exceptions.RequestException: Si ocurre un error al realizar la solicitud HTTP.
        """
        data = {
            "cfdi_uuid": cfdi_uuid,
            "motivo": motivo,
            "folioSustituto": folio_sustituto
        }
        return make_request(self.api_key, self.secret_key, self.base_url, 'POST', 'cfdi_cancel', data=data)

    def cancel_status(self, cfdi_uuid):
        """
        Verifica el estado de cancelación de una factura.

        Args:
            cfdi_uuid (str): El UID de la factura de la cual se desea verificar el estado de cancelación.

        Returns:
            dict: Un diccionario que contiene la respuesta del estado de cancelación de la factura en formato JSON.

        Raises:
            requests.exceptions.RequestException: Si ocurre un error al realizar la solicitud HTTP.
        """
        return make_request(self.api_key, self.secret_key, self.base_url, 'GET', 'cfdi_cancel_status', params=cfdi_uuid)
