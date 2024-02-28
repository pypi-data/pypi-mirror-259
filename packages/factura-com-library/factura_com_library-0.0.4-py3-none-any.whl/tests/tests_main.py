import unittest
from factura_com import api


class TestFacturaComClient(unittest.TestCase):
    def setUp(self):
        self.api_key = "JDJ5JDEwJGI0M21DbjNFbTUvTFZISmx6WnB0VmVhMGlnTlczcHBmelE2TXk3ZnRVRXNtVGtueldjaS9H"
        self.secret_key = "JDJ5JDEwJE1aTGFhWE5VM0lFaVNkMjVzZzB1d2V6YnpDSGlkc1BMSFQwbWlFRFpoLzdQd29IeVpUb3Yy"
        self.sandbox_url = "https://sandbox.factura.com/api/v4"
        self.client = api.FacturaComClient(self.api_key, self.secret_key, url=self.sandbox_url)

    def test_create_invoice(self):
        # Datos de prueba para crear una factura
        invoice_data = {
            "Receptor": {
                "ResidenciaFiscal": "",
                "UID": "55c0fdc67593d"
            },
            "TipoDocumento": "factura",
            "BorradorSiFalla": "1",
            "Draft": "1",
            "Conceptos": [
                {
                    "ClaveProdServ": "43232408",
                    "NoIdentificacion": "0021",
                    "Cantidad": "1.000000",
                    "ClaveUnidad": "E48",
                    "Unidad": "Unidad de servicio",
                    "Descripcion": "Desarrollo web a la medida",
                    "ValorUnitario": "15000.000000",
                    "Importe": "15000.000000",
                    "Descuento": "0",
                    "Impuestos": {
                        "Traslados": [
                            {
                                "Base": "15000.000000",
                                "Impuesto": "002",
                                "TipoFactor": "Tasa",
                                "TasaOCuota": "0.16",
                                "Importe": "2400.000000"
                            }
                        ],
                        "Retenidos": [],
                        "Locales": []
                    }
                }
            ],
            "UsoCFDI": "G01",
            "Serie": 1247,
            "FormaPago": "01",
            "MetodoPago": "PUE",
            "CondicionesDePago": "Pago en 9 meses",
            "CfdiRelacionados": {
                "TipoRelacion": "01",
                "UUID": [
                    "29c98cb2-f72a-4cbe-a297-606da335e187",
                    "a96f6b9a-70aa-4f2d-bc5e-d54fb7371236"
                ]
            },
            "Moneda": "MXN",
            "TipoCambio": "19.85",
            "NumOrder": "85abf36",
            "Fecha": "2020-03-20T12:53:23",
            "Comentarios": "El pedido aún no es entregado",
            "Cuenta": "0025",
            "EnviarCorreo": "true",
            "LugarExpedicion": "12345"
        }
        result = self.client.create_invoice_4_0(invoice_data)
        # Asegúrate de que la factura se haya creado correctamente
        self.assertTrue(result['success'])

    def test_cancel_invoice(self):
        # Datos de prueba para cancelar una factura
        cfdi_uuid = '55c0fdc67593d'
        motivo = '01'
        folio_sustituto = '3336cbb9-ebd4-45e8-b60b-e7bfa6f6b5e0'
        result = self.client.cancel_invoice(cfdi_uuid, motivo, folio_sustituto)
        # Asegúrate de que la factura se haya cancelado correctamente
        self.assertTrue(result['success'])

    def test_invoice_list(self):
        result = self.client.get_invoice_list()
        self.assertTrue(result['success'])


if __name__ == '__main__':
    unittest.main()
