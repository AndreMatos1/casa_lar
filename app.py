import streamlit as st


st.set_page_config(page_title="Irma Carmen Casa Lar", layout="wide")


ALUNOS = [
    {
        "id": "ALU-001",
        "nome": "Livia Santos",
        "idade": 8,
        "responsavel": "Mariana Santos",
        "telefone": "(11) 90000-0101",
        "oficinas": "Ballet, Violao",
        "turma": "Ballet Infantil A",
        "status": "Ativo",
    },
    {
        "id": "ALU-002",
        "nome": "Rafael Oliveira",
        "idade": 11,
        "responsavel": "Carlos Oliveira",
        "telefone": "(11) 90000-0202",
        "oficinas": "Futebol",
        "turma": "Sub-12 Futebol",
        "status": "Ativo",
    },
    {
        "id": "ALU-003",
        "nome": "Ana Beatriz Lima",
        "idade": 10,
        "responsavel": "Patricia Lima",
        "telefone": "(11) 90000-0303",
        "oficinas": "Dancas Urbanas, Artes",
        "turma": "Dancas Urbanas I",
        "status": "Pendente",
    },
]


TURMAS = [
    {
        "oficina": "Dancas",
        "modalidade": "Ballet",
        "turma": "Ballet Infantil A",
        "professor": "Camila Rocha",
        "dias": "Terca e Quinta",
        "horario": "09:00 - 10:15",
        "local": "Sala de Danca",
        "vagas": 20,
        "matriculados": 12,
    },
    {
        "oficina": "Esportes",
        "modalidade": "Futebol",
        "turma": "Sub-12 Futebol",
        "professor": "Diego Martins",
        "dias": "Segunda, Quarta e Sexta",
        "horario": "08:00 - 09:30",
        "local": "Campo Principal",
        "vagas": 25,
        "matriculados": 18,
    },
    {
        "oficina": "Musica",
        "modalidade": "Violao",
        "turma": "Violao Iniciante",
        "professor": "Marcos Araujo",
        "dias": "Segunda",
        "horario": "14:00 - 15:30",
        "local": "Sala de Musica",
        "vagas": 15,
        "matriculados": 9,
    },
]


AGENDA = [
    {
        "data": "2026-06-15",
        "tipo": "Aula",
        "atividade": "Ballet Infantil A",
        "horario": "09:00",
        "local": "Sala de Danca",
    },
    {
        "data": "2026-06-16",
        "tipo": "Treino",
        "atividade": "Treino Sub-12 Futebol",
        "horario": "08:00",
        "local": "Campo Principal",
    },
    {
        "data": "2026-06-20",
        "tipo": "Jogo",
        "atividade": "Casa Lar x Projeto Esperanca",
        "horario": "10:00",
        "local": "Campo Municipal",
    },
]


JOGOS = [
    {
        "categoria": "Sub-12",
        "competicao": "Liga Amistosa Regional",
        "data": "2026-06-20",
        "adversario": "Projeto Esperanca",
        "status": "Agendado",
        "placar": "-",
    },
    {
        "categoria": "Sub-14",
        "competicao": "Copa Solidariedade",
        "data": "2026-06-08",
        "adversario": "Escola Vida",
        "status": "Finalizado",
        "placar": "3 x 1",
    },
]


FICHAS = [
    {
        "arquivo": "ficha_livia_santos.pdf",
        "nome_detectado": "Livia Santos",
        "responsavel_detectado": "Mariana Santos",
        "status": "Revisao pendente",
        "confianca": "86%",
    },
    {
        "arquivo": "ficha_ana_beatriz.jpg",
        "nome_detectado": "Ana Beatriz Lima",
        "responsavel_detectado": "Patricia Lima",
        "status": "Revisao pendente",
        "confianca": "72%",
    },
]


def metricas():
    ativos = len([aluno for aluno in ALUNOS if aluno["status"] == "Ativo"])
    pendentes = len([aluno for aluno in ALUNOS if aluno["status"] == "Pendente"])
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Alunos ativos", ativos)
    col2.metric("Cadastros pendentes", pendentes)
    col3.metric("Turmas", len(TURMAS))
    col4.metric("Jogos", len(JOGOS))


def inicio():
    st.title("Irma Carmen Casa Lar")
    st.caption(
        "Prototipo inicial em Streamlit com dados ficticios para apresentacao e discussao com a instituicao."
    )
    metricas()

    st.subheader("Proximas atividades")
    st.dataframe(AGENDA, use_container_width=True, hide_index=True)

    st.subheader("Objetivo desta versao")
    st.write(
        "Validar com professores, gestores e diretores os principais fluxos: "
        "cadastro de alunos, turmas, agenda, futebol, digitalizacao de fichas "
        "e comunicacao com responsaveis."
    )


def alunos():
    st.header("Alunos")
    busca = st.text_input("Buscar aluno, responsavel, turma ou oficina")
    filtrados = ALUNOS
    if busca:
        termo = busca.lower()
        filtrados = [aluno for aluno in ALUNOS if termo in str(aluno).lower()]
    st.dataframe(filtrados, use_container_width=True, hide_index=True)

    st.subheader("Cadastro demonstrativo")
    with st.form("cadastro_aluno"):
        nome = st.text_input("Nome da crianca")
        responsavel = st.text_input("Responsavel")
        telefone = st.text_input("WhatsApp")
        turma = st.selectbox("Turma", [item["turma"] for item in TURMAS])
        enviar = st.form_submit_button("Salvar cadastro de teste")
        if enviar:
            st.success(f"Cadastro de {nome or 'novo aluno'} simulado com sucesso.")


def oficinas():
    st.header("Oficinas e turmas")
    st.dataframe(TURMAS, use_container_width=True, hide_index=True)

    st.subheader("Estrutura sugerida")
    st.write("Oficinas > Modalidades > Turmas > Alunos > Agenda")


def agenda():
    st.header("Agenda e recados")
    st.dataframe(AGENDA, use_container_width=True, hide_index=True)

    st.subheader("Enviar recado demonstrativo")
    st.selectbox("Aluno", [item["nome"] for item in ALUNOS])
    st.text_area(
        "Mensagem",
        "Ola, temos um comunicado da Casa Lar sobre a proxima atividade.",
    )
    st.button("Simular envio por WhatsApp")
    st.info(
        "Na versao real, podemos integrar WhatsApp Cloud API, Twilio, Z-API ou outro provedor."
    )


def futebol():
    st.header("Futebol")
    st.dataframe(JOGOS, use_container_width=True, hide_index=True)

    st.subheader("Registrar resultado demonstrativo")
    jogo = st.selectbox(
        "Jogo",
        [f"{item['categoria']} - {item['adversario']}" for item in JOGOS],
    )
    placar = st.text_input("Placar", placeholder="Ex.: 2 x 1")
    if st.button("Salvar resultado de teste"):
        st.success(f"Resultado {placar or '-'} registrado para {jogo}.")


def digitalizacao():
    st.header("Digitalizacao de fichas")
    st.caption(
        "Fluxo inicial para receber fichas fisicas digitalizadas e revisar dados extraidos."
    )
    st.file_uploader("Enviar ficha digitalizada", type=["pdf", "png", "jpg", "jpeg"])
    st.dataframe(FICHAS, use_container_width=True, hide_index=True)

    ficha = st.selectbox("Ficha para revisar", [item["arquivo"] for item in FICHAS])
    st.text_input("Nome revisado")
    st.text_input("Responsavel revisado")
    if st.button("Aprovar ficha de teste"):
        st.success(f"Ficha {ficha} aprovada para cadastro.")


def dashboard():
    st.header("Dashboard da direcao")
    metricas()

    st.subheader("Alunos por status")
    status = {}
    for aluno in ALUNOS:
        status[aluno["status"]] = status.get(aluno["status"], 0) + 1
    st.bar_chart(status)

    st.subheader("Matriculas por turma")
    st.bar_chart({turma["turma"]: turma["matriculados"] for turma in TURMAS})


perfil = st.sidebar.selectbox("Perfil", ["Professor", "Gestor", "Diretor"])

paginas = [
    "Inicio",
    "Alunos",
    "Oficinas e turmas",
    "Agenda e recados",
    "Futebol",
    "Digitalizacao de fichas",
]
if perfil == "Diretor":
    paginas.append("Dashboard")

pagina = st.sidebar.radio("Navegacao", paginas)
st.sidebar.caption(f"Perfil ativo: {perfil}")

if pagina == "Inicio":
    inicio()
elif pagina == "Alunos":
    alunos()
elif pagina == "Oficinas e turmas":
    oficinas()
elif pagina == "Agenda e recados":
    agenda()
elif pagina == "Futebol":
    futebol()
elif pagina == "Digitalizacao de fichas":
    digitalizacao()
elif pagina == "Dashboard":
    dashboard()
