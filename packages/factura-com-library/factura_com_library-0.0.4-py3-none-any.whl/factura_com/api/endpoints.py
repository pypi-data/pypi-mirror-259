class Endpoints:
    def __init__(self, base_url):
        """
        Inicializa un objeto Endpoints con la URL base de la API.

        Args:
            base_url (str): La URL base de la API.
        """
        self.base_url = base_url.rstrip('/')

    def cfdi_list(self):
        """
        Genera la URL para obtener la lista de facturas.

        Returns:
            str: La URL completa para obtener la lista de facturas.
        """
        return f"{self.base_url}/cfdi/list"

    def cfdi_uid(self, uid):
        """
        Genera la URL para obtener una factura por su UID.

        Args:
            uid (str): El UID de la factura que se desea obtener.

        Returns:
            str: La URL completa para obtener la factura por su UID.
        """
        return f"{self.base_url}/cfdi/uid/{uid}"

    def cfdi_uuid(self, uuid):
        """
        Genera la URL para obtener una factura por su UUID.

        Args:
            uuid (str): El UUID de la factura que se desea obtener.

        Returns:
            str: La URL completa para obtener la factura por su UUID.
        """
        return f"{self.base_url}/cfdi/uuid/{uuid}"

    def cfdi_folio(self, folio):
        """
        Genera la URL para obtener una factura por su folio.

        Args:
            folio (str): El folio de la factura que se desea obtener.

        Returns:
            str: La URL completa para obtener la factura por su folio.
        """
        return f"{self.base_url}/cfdi/folio/{folio}"

    def cfdi_create(self):
        """
        Genera la URL para crear una nueva factura.

        Returns:
            str: La URL completa para crear una nueva factura.
        """
        return f"{self.base_url}/cfdi40/create"

    def cfdi_pdf(self, cfdi_uuid):
        """
        Genera la URL para obtener el PDF de una factura por su UUID.

        Args:
            cfdi_uuid (str): El UUID de la factura de la cual se desea obtener el PDF.

        Returns:
            str: La URL completa para obtener el PDF de la factura por su UUID.
        """
        return f"{self.base_url}/cfdi40/{cfdi_uuid}/pdf"

    def cfdi_xml(self, cfdi_uuid):
        """
        Genera la URL para obtener el XML de una factura por su UUID.

        Args:
            cfdi_uuid (str): El UUID de la factura de la cual se desea obtener el XML.

        Returns:
            str: La URL completa para obtener el XML de la factura por su UUID.
        """
        return f"{self.base_url}/cfdi40/{cfdi_uuid}/xml"

    def cfdi_cancel(self, cfdi_uuid):
        """
        Genera la URL para cancelar una factura.

        Args:
            cfdi_uuid (str): El UUID de la factura que se desea cancelar.

        Returns:
            str: La URL completa para cancelar la factura.
        """
        return f"{self.base_url}/cfdi40/{cfdi_uuid}/cancel"

    def cfdi_cancel_status(self, uuid):
        """
        Genera la URL para verificar el estado de cancelación de una factura.

        Args:
            uuid (str): El UID de la factura de la cual se desea verificar el estado de cancelación.

        Returns:
            str: La URL completa para verificar el estado de cancelación de la factura.
        """
        return f"{self.base_url}/cfdi40/{uuid}/cancel_status"
