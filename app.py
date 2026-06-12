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


TREINOS = [
    {
        "categoria": "Sub-12",
        "data": "2026-06-18",
        "horario": "08:00",
        "tipo": "Treino tecnico",
        "local": "Campo Principal",
    },
    {
        "categoria": "Sub-14",
        "data": "2026-06-21",
        "horario": "15:00",
        "tipo": "Treino extra",
        "local": "Campo Principal",
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


MENU_POR_PERFIL = {
    "Professor": ["Inicio", "Alunos", "Oficinas", "Futebol"],
    "Gestor": [
        "Inicio",
        "Gestao de matriculas",
        "Alunos",
        "Oficinas",
        "Agenda",
        "Futebol",
        "Digitalizacao",
    ],
    "Diretor": [
        "Inicio",
        "Dashboard",
        "Gestao de matriculas",
        "Alunos",
        "Oficinas",
        "Agenda",
        "Futebol",
        "Digitalizacao",
    ],
}


SUBMENUS = {
    "Alunos": ["Consulta", "Cadastro", "Documentos"],
    "Oficinas": ["Turmas", "Horarios", "Professores"],
    "Agenda": ["Aulas", "Jogos", "Treinos", "Recados"],
    "Futebol": ["Turmas", "Agenda jogo", "Agenda treinos", "Resultados"],
    "Gestao de matriculas": ["Inscricoes", "Incluir em turma", "Pendencias"],
    "Digitalizacao": ["Enviar ficha", "Revisar dados", "Aprovar cadastro"],
    "Dashboard": ["Indicadores", "Oficinas", "Esportivo"],
}


def aplicar_estilo():
    st.markdown(
        """
        <style>
        div.stButton > button {
            width: 100%;
            border-radius: 6px;
            border: 1px solid #d5dbe5;
            background: #f7f9fc;
            color: #1d2733;
            font-weight: 600;
            padding: 0.58rem 0.75rem;
        }
        div.stButton > button:hover {
            border-color: #2563eb;
            color: #1746a2;
            background: #eef4ff;
        }
        section[data-testid="stSidebar"] div.stButton > button {
            justify-content: flex-start;
            text-align: left;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def selecionar_pagina(perfil):
    paginas = MENU_POR_PERFIL[perfil]
    if "pagina" not in st.session_state or st.session_state.pagina not in paginas:
        st.session_state.pagina = paginas[0]

    st.sidebar.title("Casa Lar")
    st.sidebar.caption("Menu por perfil")

    for pagina in paginas:
        if st.sidebar.button(pagina, key=f"menu_{pagina}", use_container_width=True):
            st.session_state.pagina = pagina
            st.session_state.subpagina = SUBMENUS.get(pagina, ["Principal"])[0]

    st.sidebar.divider()
    st.sidebar.caption(f"Perfil ativo: {perfil}")
    return st.session_state.pagina


def botoes_submenu(pagina):
    opcoes = SUBMENUS.get(pagina, ["Principal"])
    chave = f"subpagina_{pagina}"
    if chave not in st.session_state or st.session_state[chave] not in opcoes:
        st.session_state[chave] = opcoes[0]

    cols = st.columns(len(opcoes))
    for col, opcao in zip(cols, opcoes):
        if col.button(opcao, key=f"{pagina}_{opcao}", use_container_width=True):
            st.session_state[chave] = opcao

    return st.session_state[chave]


def tabela_fechada(titulo, dados):
    with st.expander(titulo, expanded=False):
        st.dataframe(dados, use_container_width=True, hide_index=True)


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
    tabela_fechada("Abrir proximas atividades", AGENDA)

    st.subheader("Objetivo desta versao")
    st.write(
        "Validar os principais fluxos: cadastro de alunos, matriculas, oficinas, "
        "agenda, futebol, digitalizacao de fichas e comunicacao com responsaveis."
    )


def alunos():
    st.header("Alunos")
    subpagina = botoes_submenu("Alunos")

    if subpagina == "Consulta":
        busca = st.text_input("Buscar aluno, responsavel, turma ou oficina")
        filtrados = ALUNOS
        if busca:
            termo = busca.lower()
            filtrados = [aluno for aluno in ALUNOS if termo in str(aluno).lower()]
        tabela_fechada("Abrir tabela de alunos", filtrados)

    elif subpagina == "Cadastro":
        with st.form("cadastro_aluno"):
            nome = st.text_input("Nome da crianca")
            responsavel = st.text_input("Responsavel")
            telefone = st.text_input("WhatsApp")
            turma = st.selectbox("Turma", [item["turma"] for item in TURMAS])
            enviar = st.form_submit_button("Salvar cadastro de teste")
            if enviar:
                st.success(f"Cadastro de {nome or 'novo aluno'} simulado com sucesso.")

    elif subpagina == "Documentos":
        tabela_fechada("Abrir documentos pendentes", FICHAS)
        st.file_uploader("Enviar documento do aluno", type=["pdf", "png", "jpg", "jpeg"])


def oficinas():
    st.header("Oficinas")
    subpagina = botoes_submenu("Oficinas")

    if subpagina == "Turmas":
        tabela_fechada("Abrir tabela de turmas", TURMAS)
    elif subpagina == "Horarios":
        horarios = [
            {
                "turma": item["turma"],
                "dias": item["dias"],
                "horario": item["horario"],
                "local": item["local"],
            }
            for item in TURMAS
        ]
        tabela_fechada("Abrir horarios das oficinas", horarios)
    elif subpagina == "Professores":
        professores = [
            {
                "professor": item["professor"],
                "oficina": item["oficina"],
                "modalidade": item["modalidade"],
                "turma": item["turma"],
            }
            for item in TURMAS
        ]
        tabela_fechada("Abrir professores e turmas", professores)


def agenda():
    st.header("Agenda")
    subpagina = botoes_submenu("Agenda")

    if subpagina == "Aulas":
        tabela_fechada("Abrir agenda de aulas", [item for item in AGENDA if item["tipo"] == "Aula"])
    elif subpagina == "Jogos":
        tabela_fechada("Abrir agenda de jogos", [item for item in AGENDA if item["tipo"] == "Jogo"])
    elif subpagina == "Treinos":
        tabela_fechada("Abrir agenda de treinos", TREINOS)
    elif subpagina == "Recados":
        st.selectbox("Aluno", [item["nome"] for item in ALUNOS])
        st.text_area(
            "Mensagem",
            "Ola, temos um comunicado da Casa Lar sobre a proxima atividade.",
        )
        st.button("Simular envio por WhatsApp")
        st.info("Na versao real, podemos integrar WhatsApp Cloud API, Twilio, Z-API ou outro provedor.")


def futebol():
    st.header("Futebol")
    subpagina = botoes_submenu("Futebol")

    if subpagina == "Turmas":
        futebol_turmas = [item for item in TURMAS if item["modalidade"] == "Futebol"]
        tabela_fechada("Abrir turmas de futebol", futebol_turmas)
    elif subpagina == "Agenda jogo":
        tabela_fechada("Abrir agenda de jogos", JOGOS)
    elif subpagina == "Agenda treinos":
        tabela_fechada("Abrir agenda de treinos", TREINOS)
    elif subpagina == "Resultados":
        tabela_fechada("Abrir resultados", [item for item in JOGOS if item["status"] == "Finalizado"])
        st.subheader("Registrar resultado demonstrativo")
        jogo = st.selectbox(
            "Jogo",
            [f"{item['categoria']} - {item['adversario']}" for item in JOGOS],
        )
        placar = st.text_input("Placar", placeholder="Ex.: 2 x 1")
        if st.button("Salvar resultado de teste"):
            st.success(f"Resultado {placar or '-'} registrado para {jogo}.")


def gestao_matriculas():
    st.header("Gestao de matriculas")
    subpagina = botoes_submenu("Gestao de matriculas")

    if subpagina == "Inscricoes":
        tabela_fechada("Abrir inscricoes recebidas", ALUNOS)
    elif subpagina == "Incluir em turma":
        aluno = st.selectbox("Aluno", [item["nome"] for item in ALUNOS])
        turma = st.selectbox("Turma", [item["turma"] for item in TURMAS])
        if st.button("Incluir aluno na turma"):
            st.success(f"{aluno} incluido em {turma} para demonstracao.")
    elif subpagina == "Pendencias":
        pendentes = [item for item in ALUNOS if item["status"] == "Pendente"]
        tabela_fechada("Abrir pendencias de matricula", pendentes)


def digitalizacao():
    st.header("Digitalizacao")
    subpagina = botoes_submenu("Digitalizacao")

    if subpagina == "Enviar ficha":
        st.file_uploader("Enviar ficha digitalizada", type=["pdf", "png", "jpg", "jpeg"])
        st.info("Nesta versao, o envio e demonstrativo. Depois podemos incluir OCR.")
    elif subpagina == "Revisar dados":
        tabela_fechada("Abrir fichas para revisao", FICHAS)
        st.text_input("Nome revisado")
        st.text_input("Responsavel revisado")
    elif subpagina == "Aprovar cadastro":
        ficha = st.selectbox("Ficha para aprovar", [item["arquivo"] for item in FICHAS])
        if st.button("Aprovar ficha de teste"):
            st.success(f"Ficha {ficha} aprovada para cadastro.")


def dashboard():
    st.header("Dashboard da direcao")
    subpagina = botoes_submenu("Dashboard")

    if subpagina == "Indicadores":
        metricas()
        st.subheader("Alunos por status")
        status = {}
        for aluno in ALUNOS:
            status[aluno["status"]] = status.get(aluno["status"], 0) + 1
        st.bar_chart(status)
    elif subpagina == "Oficinas":
        st.subheader("Matriculas por turma")
        st.bar_chart({turma["turma"]: turma["matriculados"] for turma in TURMAS})
        tabela_fechada("Abrir dados das oficinas", TURMAS)
    elif subpagina == "Esportivo":
        st.subheader("Resumo esportivo")
        tabela_fechada("Abrir jogos e resultados", JOGOS)


aplicar_estilo()
perfil = st.sidebar.selectbox("Perfil", ["Professor", "Gestor", "Diretor"])
pagina = selecionar_pagina(perfil)

if pagina == "Inicio":
    inicio()
elif pagina == "Alunos":
    alunos()
elif pagina == "Oficinas":
    oficinas()
elif pagina == "Agenda":
    agenda()
elif pagina == "Futebol":
    futebol()
elif pagina == "Gestao de matriculas":
    gestao_matriculas()
elif pagina == "Digitalizacao":
    digitalizacao()
elif pagina == "Dashboard":
    dashboard()
