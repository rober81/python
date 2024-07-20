import requests

def call_operaciones_de_cambio():
    url = 'http://localhost/devtools/operacionesdecambio/alertas'
    cuit_entidad = '30500010912'
    cuit_empresa = '30506730038'
    url_final = f"{url}/{cuit_entidad}/{cuit_empresa}"
    call_api(url_final)

def call_api(url, headers=None):
    print(f"Llamando api: {url}")
    if headers:
        response = requests.get(url, headers=headers)
    else:
        response = requests.get(url)
    print(response.json()) 

def call_bcra_healthcheck():
    token = "eyJhbGciOiJSU0EtT0FFUCIsImVuYyI6IkEyNTZDQkMtSFM1MTIiLCJ0eXAiOiJKV1QifQ.1YogPaUp4SgMJtNIqdj8Rsnym5IWpj87YKA5pGMHA89Wg-EoFz8zdNWP48iwNU-egAzdKqfNz5fGkLg8vQfnW-9kEpudCgk3Snn8BTRTAok1xaEL_-jQ74dbQbRevI0375vJOscatodVZtCM7v_H0h3CefnUe4-7SgGyBTNOHmoNxwUI3lmczqnULG4OH27FNfTsSrYcWwjLqCfxDhx4ZOXkExt-VVGzP2r1UidHtsrL-O59TLAX4678I7e5jjy9Z4hJ15G3djcIqyair0nweJz_6JAznqx7P8RhwgSMjN-n62uA_hhG_CAgI4W26ky-k4okEkNDoTZe1sGNmMdKng.edu5nMPCDiXtnejvfkHQtg.Fnpn4W6ae1DuXGDIBlO_Ehdhg4LSNYQquPmgzp8LWDW-yFrIFHFUTjY8rsxQfEvovurF8kDMbn3qv5R2ZS-HPWtPXjUoi8A-VFDKeHR0UWRVuSSooZwDNDSlKGUfLYBruEhoiWK9bfGSRgWOytnd8W5eCkqhG7l0JXTX0DLfL0JLUhYuYVgNo-WTDu6JHssxPttbPtO1aY48Pw88ob7_Dyx1CPbqwU2NE2pWc8woU37ELEhTnWdnYHUqHH9urAU3oO0Ms_dcHeqq19q2WPNC8DzY4WuJk2jjB_K5WBNoZVCqYRGFyhY20KYCaazGInt_dBTfh11Wzk20xSB0ib9p6FAGU8FS8CXJbRUJ7bqiVhhx27LQIdPhaqLL4KPPgjIsEk45IYZfOWg48JX33nOegWU1OJHqEcyrAAmUt4jzCoa14er22v1zrwjkmwq43zdk4_mnsfwoL_YAazmaZfk1hOcH9OXijgL0UQEBslPczhSwjf7wWqEtvFkktOPRKXqOZ8ownDpqvBnOMpArw9H-AztX1grPniJdH2maZTEnIwNN-4JIYRXSHlnCERlqxRKHJNl4nYpsGJlFplSM-CotlHXAFwFvQWt-6htaKY7MRe25fRzLnkYkIfZXt7nZ8WJEoqxptpEadgQqD3GZ6Ca3P4WjPZxMoiM0szvOLLMQTQiji1X_DXXSFcKkpVepGu1JFH81Q_J7PYN-YyneyMpsSeX4G3EGzeV1-inZN5LFsPILIWG4DNyBOHN2QGBEEwArep_2mJLXjaMo_5ePojk_C6COIpK_7u64PYnNXwXiP8j6SFeMUiT599KsHE5rfJKDBgtsm7cDZP0HaCRxCpzGXw.rff9rNoiJpqd6B_d8O5P8MSQVbCxHsUuJHTwLEZoZDE"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    bcra_url_healthcheck ="https://controlcambiorest.homologacion.bcra.sfa/api/healthcheck"
    call_api(bcra_url_healthcheck, headers)
    verificador_url_healthcheck="https://verificador.homologacion.bcra.sfa/api/healthcheck"
    call_api(verificador_url_healthcheck, headers)


if __name__ == '__main__':
    call_bcra_healthcheck()

