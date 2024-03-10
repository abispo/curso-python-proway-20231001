
def gerar_lista_horarios():

    horarios = []

    for hora in range(0, 24):
        horarios.append({
            "hora": f"{hora:02d}:00",
            "agendas": [
                None for _ in range(7)
            ]
        })

    return horarios