import requests
from .endpoints import Endpoints


def make_request(api_key, secret_key, url, method, endpoint, params=None, data=None):
    base_url = url.rstrip('/')
    endpoints = Endpoints(base_url)
    headers = {
        "Content-Type": "application/json",
        "F-PLUGIN": "9d4095c8f7ed5785cb14c0e3b033eeb8252416ed",
        "F-Api-Key": api_key,
        "F-Secret-Key": secret_key
    }
    endpoint_methods = {
        'cfdi_list': endpoints.cfdi_list,
        'cfdi_uid': lambda: endpoints.cfdi_uid(params),
        'cfdi_uuid': lambda: endpoints.cfdi_uuid(params),
        'cfdi_folio': lambda: endpoints.cfdi_folio(params),
        'cfdi_create': endpoints.cfdi_create,
        'cfdi_pdf': lambda: endpoints.cfdi_pdf(params),
        'cfdi_xml': lambda: endpoints.cfdi_xml(params),
        'cfdi_cancel': lambda: endpoints.cfdi_cancel(params),  # Llamar al método con cfdi_uuid como parámetro
        'cfdi_cancel_status': lambda: endpoints.cfdi_cancel_status(params),  # Llamar al método con cfdi_uuid como parámetro
    }
    request_url = endpoint_methods.get(endpoint, lambda: base_url)()
    response = None
    try:
        if method == 'GET':
            response = requests.get(request_url, headers=headers, params=params)
        elif method == 'POST':
            response = requests.post(request_url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud {method} en {request_url}:", e)
        return None
