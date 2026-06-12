from datetime import date
from pathlib import Path
import streamlit as st


LOGO_PATH = Path(__file__).parent / "assets" / "logo.png"

st.set_page_config(
    page_title="Irma Carmen Casa Lar",
    page_icon=str(LOGO_PATH),
    layout="wide",
)


ALUNOS = [
    {
        "id": "ALU-001",
        "nome": "Livia Santos",
        "idade": 8,
        "responsavel": "Mariana Santos",
        "telefone": "(11) 90000-0101",
        "oficina": "Dancas",
        "modalidade": "Ballet",
        "turma": "Ballet Infantil A",
        "professor": "Camila Rocha",
        "status": "Ativo",
    },
    {
        "id": "ALU-002",
        "nome": "Rafael Oliveira",
        "idade": 11,
        "responsavel": "Carlos Oliveira",
        "telefone": "(11) 90000-0202",
        "oficina": "Esportes",
        "modalidade": "Futebol",
        "turma": "Sub-12 Futebol",
        "professor": "Diego Martins",
        "status": "Ativo",
    },
    {
        "id": "ALU-003",
        "nome": "Ana Beatriz Lima",
        "idade": 10,
        "responsavel": "Patricia Lima",
        "telefone": "(11) 90000-0303",
        "oficina": "Dancas",
        "modalidade": "Dancas Urbanas",
        "turma": "Dancas Urbanas I",
        "professor": "Camila Rocha",
        "status": "Pendente",
    },
    {
        "id": "ALU-004",
        "nome": "Joao Pedro Costa",
        "idade": 13,
        "responsavel": "Fernanda Costa",
        "telefone": "(11) 90000-0404",
        "oficina": "Esportes",
        "modalidade": "Futebol",
        "turma": "Sub-14 Futebol",
        "professor": "Diego Martins",
        "status": "Ativo",
    },
    {
        "id": "ALU-005",
        "nome": "Clara Nascimento",
        "idade": 7,
        "responsavel": "Renata Nascimento",
        "telefone": "(11) 90000-0505",
        "oficina": "Dancas",
        "modalidade": "Ballet",
        "turma": "Ballet Infantil A",
        "professor": "Camila Rocha",
        "status": "Ativo",
    },
]


TURMAS = [
    {
        "oficina": "Dancas",
        "modalidade": "Ballet",
        "turma": "Ballet Infantil A",
        "professor": "Camila Rocha",
        "dias": ["Segunda", "Quarta"],
        "horario": "09:00 - 10:15",
        "local": "Sala de Danca",
        "vagas": 20,
        "matriculados": 12,
    },
    {
        "oficina": "Dancas",
        "modalidade": "Dancas Urbanas",
        "turma": "Dancas Urbanas I",
        "professor": "Camila Rocha",
        "dias": ["Terca", "Quinta"],
        "horario": "10:30 - 11:30",
        "local": "Sala de Danca",
        "vagas": 18,
        "matriculados": 11,
    },
    {
        "oficina": "Esportes",
        "modalidade": "Futebol",
        "turma": "Sub-12 Futebol",
        "professor": "Diego Martins",
        "dias": ["Segunda", "Quarta", "Sexta"],
        "horario": "08:00 - 09:30",
        "local": "Campo Principal",
        "vagas": 25,
        "matriculados": 18,
    },
    {
        "oficina": "Esportes",
        "modalidade": "Futebol",
        "turma": "Sub-14 Futebol",
        "professor": "Diego Martins",
        "dias": ["Terca", "Quinta"],
        "horario": "15:30 - 17:00",
        "local": "Campo Principal",
        "vagas": 25,
        "matriculados": 21,
    },
    {
        "oficina": "Musica",
        "modalidade": "Violao",
        "turma": "Violao Iniciante",
        "professor": "Marcos Araujo",
        "dias": ["Segunda"],
        "horario": "14:00 - 15:30",
        "local": "Sala de Musica",
        "vagas": 15,
        "matriculados": 9,
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


DIAS_SEMANA = ["Segunda", "Terca", "Quarta", "Quinta", "Sexta", "Sabado"]
DIA_ATUAL_DEMO = "Sexta"


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
    "Alunos": ["Consulta", "Meus alunos", "Cadastro", "Documentos"],
    "Oficinas": ["Agenda semanal", "Minhas turmas", "Chamada"],
    "Agenda": ["Aulas", "Jogos", "Treinos", "Recados"],
    "Futebol": ["Turmas", "Agenda jogo", "Agenda treinos", "Resultados", "Chamada"],
    "Gestao de matriculas": ["Inscricoes", "Incluir em turma", "Pendencias"],
    "Digitalizacao": ["Enviar ficha", "Revisar dados", "Aprovar cadastro"],
    "Dashboard": ["Indicadores", "Oficinas", "Esportivo"],
}


def aplicar_estilo():
    st.markdown(
        """
        <style>
        .block-container {
            padding-top: 1.8rem;
        }
        div.stButton > button {
            width: 100%;
            border-radius: 14px;
            border: 1px solid #cfd8e3;
            background: linear-gradient(180deg, #ffffff 0%, #f4f7fb 100%);
            color: #1d2733;
            font-weight: 700;
            min-height: 42px;
            padding: 0.62rem 0.9rem;
            box-shadow: 0 1px 2px rgba(16, 24, 40, 0.08);
        }
        div.stButton > button:hover {
            border-color: #2563eb;
            color: #1746a2;
            background: #edf4ff;
        }
        div.stButton > button:disabled {
            border-color: #1d4ed8;
            background: linear-gradient(180deg, #2563eb 0%, #1d4ed8 100%);
            color: #ffffff;
            opacity: 1;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.24);
        }
        section[data-testid="stSidebar"] div.stButton > button {
            justify-content: flex-start;
            text-align: left;
        }
        section[data-testid="stSidebar"] div[role="radiogroup"] {
            gap: 8px;
        }
        section[data-testid="stSidebar"] label[data-baseweb="radio"] {
            width: 100%;
            min-height: 46px;
            margin: 0 0 8px 0;
            padding: 0 14px;
            border-radius: 14px;
            border: 1px solid #cfd8e3;
            background: linear-gradient(180deg, #ffffff 0%, #f4f7fb 100%);
            box-shadow: 0 1px 2px rgba(16, 24, 40, 0.08);
            display: flex;
            align-items: center;
        }
        section[data-testid="stSidebar"] label[data-baseweb="radio"]:hover {
            border-color: #2563eb;
            background: #edf4ff;
        }
        section[data-testid="stSidebar"] label[data-baseweb="radio"]:has(input:checked) {
            border-color: #1d4ed8;
            background: linear-gradient(180deg, #2563eb 0%, #1d4ed8 100%);
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.24);
        }
        section[data-testid="stSidebar"] label[data-baseweb="radio"]:has(input:checked) p {
            color: #ffffff;
        }
        section[data-testid="stSidebar"] label[data-baseweb="radio"] p {
            color: #1d2733;
            font-weight: 700;
        }
        section[data-testid="stSidebar"] label[data-baseweb="radio"] > div:first-child {
            display: none;
        }
        a.nav-link, a.side-nav-link {
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 42px;
            width: 100%;
            border-radius: 14px;
            border: 1px solid #cfd8e3;
            background: linear-gradient(180deg, #ffffff 0%, #f4f7fb 100%);
            color: #1d2733 !important;
            font-weight: 700;
            text-decoration: none !important;
            padding: 0.62rem 0.9rem;
            box-shadow: 0 1px 2px rgba(16, 24, 40, 0.08);
            margin-bottom: 8px;
            text-align: center;
        }
        a.side-nav-link {
            justify-content: flex-start;
            min-height: 46px;
        }
        a.nav-link:hover, a.side-nav-link:hover {
            border-color: #2563eb;
            color: #1746a2 !important;
            background: #edf4ff;
        }
        a.nav-link.active, a.side-nav-link.active {
            border-color: #1d4ed8;
            background: linear-gradient(180deg, #2563eb 0%, #1d4ed8 100%);
            color: #ffffff !important;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.24);
        }
        .card {
            border: 1px solid #d9e2ec;
            border-radius: 14px;
            padding: 14px 16px;
            background: #ffffff;
            box-shadow: 0 1px 3px rgba(16, 24, 40, 0.08);
            min-height: 112px;
        }
        .card strong {
            color: #0f172a;
        }
        .today-card {
            border-color: #2563eb;
            background: #eff6ff;
        }
        .muted {
            color: #667085;
            font-size: 0.9rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def exibir_logo_sidebar():
    if LOGO_PATH.exists():
        st.sidebar.image(str(LOGO_PATH), use_container_width=True)


def exibir_logo_inicio():
    if LOGO_PATH.exists():
        left, center, right = st.columns([1, 1, 1])
        center.image(str(LOGO_PATH), use_container_width=True)


def navegar_para(pagina, subpagina=None, turma=None):
    st.session_state.pagina = pagina
    if subpagina:
        st.session_state[f"subpagina_{pagina}"] = subpagina
    if turma:
        st.session_state.turma_selecionada = turma


def nav_link(label, pagina, subpagina=None, turma=None, active=False, sidebar=False, key_suffix=""):
    key = f"nav_{'side' if sidebar else 'main'}_{label}_{pagina}_{subpagina}_{turma}_{key_suffix}"
    st.button(
        label,
        key=key,
        disabled=active,
        use_container_width=True,
        on_click=navegar_para,
        args=(pagina, subpagina, turma),
    )


def aplicar_query_params(perfil):
    params = st.query_params
    pagina = params.get("page")
    subpagina = params.get("sub")
    turma = params.get("turma")
    paginas = MENU_POR_PERFIL[perfil]

    if pagina in paginas:
        st.session_state.pagina = pagina
    elif "pagina" not in st.session_state or st.session_state.pagina not in paginas:
        st.session_state.pagina = paginas[0]

    pagina_atual = st.session_state.pagina
    opcoes = SUBMENUS.get(pagina_atual, ["Principal"])
    if subpagina in opcoes:
        st.session_state[f"subpagina_{pagina_atual}"] = subpagina
    elif f"subpagina_{pagina_atual}" not in st.session_state:
        st.session_state[f"subpagina_{pagina_atual}"] = opcoes[0]

    if turma:
        st.session_state.turma_selecionada = turma


def selecionar_pagina(perfil):
    paginas = MENU_POR_PERFIL[perfil]
    if "pagina" not in st.session_state or st.session_state.pagina not in paginas:
        st.session_state.pagina = paginas[0]

    st.sidebar.title("Casa Lar")
    st.sidebar.caption("Menu por perfil")
    with st.sidebar:
        for pagina in paginas:
            nav_link(
                pagina,
                pagina,
                SUBMENUS.get(pagina, ["Principal"])[0],
                active=pagina == st.session_state.pagina,
                sidebar=True,
            )

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
        with col:
            nav_link(opcao, pagina, opcao, active=opcao == st.session_state[chave])

    return st.session_state[chave]


def tabela_fechada(titulo, dados):
    with st.expander(titulo, expanded=False):
        st.dataframe(dados, use_container_width=True, hide_index=True)


def alunos_por_turma(turma):
    return [aluno for aluno in ALUNOS if aluno["turma"] == turma]


def turmas_do_professor(professor):
    return [turma for turma in TURMAS if turma["professor"] == professor]


def alunos_do_professor(professor):
    return [aluno for aluno in ALUNOS if aluno["professor"] == professor]


def metricas():
    ativos = len([aluno for aluno in ALUNOS if aluno["status"] == "Ativo"])
    pendentes = len([aluno for aluno in ALUNOS if aluno["status"] == "Pendente"])
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Alunos ativos", ativos)
    col2.metric("Cadastros pendentes", pendentes)
    col3.metric("Turmas", len(TURMAS))
    col4.metric("Jogos", len(JOGOS))


def card_turma(turma, destino="Oficinas", subpagina="Minhas turmas", key_suffix=""):
    alunos = alunos_por_turma(turma["turma"])
    ocupacao = f"{turma['matriculados']} / {turma['vagas']} vagas"
    st.markdown(
        f"""
        <div class="card">
            <strong>{turma['turma']}</strong><br>
            <span class="muted">{turma['modalidade']} | {turma['horario']} | {turma['local']}</span><br>
            <span class="muted">{ocupacao} | {len(alunos)} alunos na amostra</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    nav_link(f"Abrir {turma['turma']}", destino, subpagina, turma["turma"], key_suffix=key_suffix)


def agenda_semanal(turmas, destino="Oficinas"):
    st.subheader("Agenda semanal")
    cols = st.columns(len(DIAS_SEMANA))
    for dia_index, (col, dia) in enumerate(zip(cols, DIAS_SEMANA)):
        eventos = [turma for turma in turmas if dia in turma["dias"]]
        classe = "card today-card" if dia == DIA_ATUAL_DEMO else "card"
        col.markdown(
            f"<div class='{classe}'><strong>{dia}</strong><br><span class='muted'>{'Hoje' if dia == DIA_ATUAL_DEMO else 'Semana'}</span></div>",
            unsafe_allow_html=True,
        )
        if not eventos:
            col.caption("Sem atividades")
        for evento_index, turma in enumerate(eventos):
            with col:
                nav_link(
                    f"{turma['horario']} | {turma['turma']}",
                    destino,
                    "Minhas turmas" if destino == "Oficinas" else "Turmas",
                    turma["turma"],
                    key_suffix=f"agenda_{destino}_{dia_index}_{evento_index}",
                )


def chamada_turma(turma_nome):
    alunos = alunos_por_turma(turma_nome)
    st.subheader(f"Chamada - {turma_nome}")
    if not alunos:
        st.info("Nenhum aluno encontrado para esta turma na base demonstrativa.")
        return

    if "chamadas_salvas" not in st.session_state:
        st.session_state.chamadas_salvas = []

    with st.form(f"chamada_{turma_nome}"):
        data_chamada = st.date_input("Data da chamada", value=date.today())
        st.caption("Marque presente ou ausente e, se necessário, registre uma observação curta por aluno.")

        header = st.columns([3, 2, 3])
        header[0].markdown("**Aluno**")
        header[1].markdown("**Presença**")
        header[2].markdown("**Observação**")

        registros = []
        for aluno in alunos:
            row = st.columns([3, 2, 3])
            row[0].write(aluno["nome"])
            status = row[1].radio(
                "Presença",
                ["Presente", "Ausente"],
                horizontal=True,
                key=f"presenca_{turma_nome}_{aluno['id']}",
                label_visibility="collapsed",
            )
            observacao = row[2].text_input(
                "Observação",
                key=f"obs_{turma_nome}_{aluno['id']}",
                label_visibility="collapsed",
                placeholder="Ex.: chegou atrasado",
            )

            registros.append(
                {
                    "data": data_chamada.isoformat(),
                    "turma": turma_nome,
                    "aluno": aluno["nome"],
                    "status": status,
                    "observacao": observacao,
                }
            )

        salvar = st.form_submit_button("Salvar chamada")

    if salvar:
        st.session_state.chamadas_salvas.extend(registros)
        presentes = len([registro for registro in registros if registro["status"] == "Presente"])
        ausentes = len([registro for registro in registros if registro["status"] == "Ausente"])
        st.success(f"Chamada salva: {presentes} presente(s), {ausentes} ausente(s).")

    historico = [
        registro
        for registro in st.session_state.get("chamadas_salvas", [])
        if registro["turma"] == turma_nome
    ]
    if historico:
        tabela_fechada("Histórico de chamadas desta turma", historico)


def inicio(perfil, professor):
    exibir_logo_inicio()
    st.title("Irma Carmen Casa Lar")
    st.caption("Prototipo inicial em Streamlit com foco na rotina de professores, gestores e diretores.")
    metricas()

    st.subheader("Atalhos")
    atalhos_padrao = ["Turmas", "Futebol", "Meus alunos", "Chamada"]
    atalhos = st.multiselect("Editar atalhos da tela inicial", atalhos_padrao, default=atalhos_padrao)
    cols = st.columns(max(len(atalhos), 1))
    for col, atalho in zip(cols, atalhos):
        with col:
            if atalho == "Turmas":
                nav_link(atalho, "Oficinas", "Minhas turmas")
            elif atalho == "Futebol":
                nav_link(atalho, "Futebol", "Turmas")
            elif atalho == "Meus alunos":
                nav_link(atalho, "Alunos", "Meus alunos")
            elif atalho == "Chamada":
                nav_link(atalho, "Oficinas", "Chamada")

    turmas = turmas_do_professor(professor) if perfil == "Professor" else TURMAS
    agenda_semanal(turmas)


def alunos(perfil, professor):
    st.header("Alunos")
    subpagina = botoes_submenu("Alunos")

    base = alunos_do_professor(professor) if perfil == "Professor" else ALUNOS

    if subpagina == "Consulta":
        with st.form("busca_aluno"):
            busca = st.text_input("Buscar aluno, responsavel, turma ou oficina")
            buscar = st.form_submit_button("Buscar")
        filtrados = base
        if buscar and busca:
            termo = busca.lower()
            filtrados = [aluno for aluno in base if termo in str(aluno).lower()]
        st.dataframe(filtrados, use_container_width=True, hide_index=True)

    elif subpagina == "Meus alunos":
        st.caption("Alunos vinculados as turmas do professor selecionado.")
        turmas = ["Todas"] + sorted({aluno["turma"] for aluno in base})
        status = ["Todos"] + sorted({aluno["status"] for aluno in base})
        col1, col2 = st.columns(2)
        filtro_turma = col1.selectbox("Filtrar por turma", turmas)
        filtro_status = col2.selectbox("Filtrar por status", status)
        filtrados = base
        if filtro_turma != "Todas":
            filtrados = [aluno for aluno in filtrados if aluno["turma"] == filtro_turma]
        if filtro_status != "Todos":
            filtrados = [aluno for aluno in filtrados if aluno["status"] == filtro_status]
        tabela_fechada("Meus alunos", filtrados)
        if filtro_turma != "Todas":
            nav_link(
                "Abrir turma selecionada",
                "Oficinas",
                "Minhas turmas",
                filtro_turma,
                key_suffix="meus_alunos",
            )

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
        tabela_fechada("Documentos pendentes", FICHAS)
        st.file_uploader("Enviar documento do aluno", type=["pdf", "png", "jpg", "jpeg"])


def oficinas(perfil, professor):
    st.header("Oficinas")
    subpagina = botoes_submenu("Oficinas")
    base_turmas = turmas_do_professor(professor) if perfil == "Professor" else TURMAS

    if subpagina == "Agenda semanal":
        agenda_semanal(base_turmas)

    elif subpagina == "Minhas turmas":
        st.caption("Acesse cada turma para ver vagas, alunos e aulas da semana.")
        modalidades = ["Todas"] + sorted({turma["modalidade"] for turma in base_turmas})
        modalidade = st.selectbox("Filtrar por oficina/modalidade", modalidades)
        turmas_filtradas = base_turmas
        if modalidade != "Todas":
            turmas_filtradas = [turma for turma in base_turmas if turma["modalidade"] == modalidade]

        cols = st.columns(2)
        for index, turma in enumerate(turmas_filtradas):
            with cols[index % 2]:
                card_turma(turma, key_suffix=f"oficinas_{index}")

        selecionada = st.session_state.get(
            "turma_selecionada",
            turmas_filtradas[0]["turma"] if turmas_filtradas else "",
        )
        if selecionada:
            st.divider()
            st.subheader(f"Detalhes da turma: {selecionada}")
            turma = next(item for item in TURMAS if item["turma"] == selecionada)
            col1, col2, col3 = st.columns(3)
            col1.metric("Vagas", turma["vagas"])
            col2.metric("Matriculados", turma["matriculados"])
            col3.metric("Alunos na amostra", len(alunos_por_turma(selecionada)))
            tabela_fechada("Alunos da turma", alunos_por_turma(selecionada))
            tabela_fechada(
                "Aulas da semana",
                [
                    {
                        "dia": dia,
                        "horario": turma["horario"],
                        "local": turma["local"],
                        "professor": turma["professor"],
                    }
                    for dia in turma["dias"]
                ],
            )

    elif subpagina == "Chamada":
        turmas = [turma["turma"] for turma in base_turmas]
        turma_padrao = st.session_state.get("turma_selecionada", turmas[0] if turmas else "")
        turma = st.selectbox("Turma", turmas, index=turmas.index(turma_padrao) if turma_padrao in turmas else 0)
        chamada_turma(turma)


def agenda():
    st.header("Agenda")
    subpagina = botoes_submenu("Agenda")

    if subpagina == "Aulas":
        agenda_semanal(TURMAS)
    elif subpagina == "Jogos":
        tabela_fechada("Agenda de jogos", JOGOS)
    elif subpagina == "Treinos":
        treinos = [turma for turma in TURMAS if turma["modalidade"] == "Futebol"]
        agenda_semanal(treinos, "Futebol")
    elif subpagina == "Recados":
        st.selectbox("Aluno", [item["nome"] for item in ALUNOS])
        st.text_area("Mensagem", "Ola, temos um comunicado da Casa Lar sobre a proxima atividade.")
        st.button("Simular envio por WhatsApp")
        st.info("Na versao real, podemos integrar WhatsApp Cloud API, Twilio, Z-API ou outro provedor.")


def futebol(perfil, professor):
    st.header("Futebol")
    subpagina = botoes_submenu("Futebol")
    futebol_turmas = [item for item in TURMAS if item["modalidade"] == "Futebol"]
    if perfil == "Professor":
        futebol_turmas = [item for item in futebol_turmas if item["professor"] == professor]

    if subpagina == "Turmas":
        cols = st.columns(2)
        for index, turma in enumerate(futebol_turmas):
            with cols[index % 2]:
                card_turma(turma, "Futebol", "Turmas", key_suffix=f"futebol_{index}")

    elif subpagina == "Agenda jogo":
        tabela_fechada("Agenda de jogos", JOGOS)

    elif subpagina == "Agenda treinos":
        agenda_semanal(futebol_turmas, "Futebol")

    elif subpagina == "Resultados":
        tabela_fechada("Resultados", [item for item in JOGOS if item["status"] == "Finalizado"])
        st.subheader("Registrar resultado demonstrativo")
        jogo = st.selectbox("Jogo", [f"{item['categoria']} - {item['adversario']}" for item in JOGOS])
        placar = st.text_input("Placar", placeholder="Ex.: 2 x 1")
        if st.button("Salvar resultado de teste"):
            st.success(f"Resultado {placar or '-'} registrado para {jogo}.")

    elif subpagina == "Chamada":
        turmas = [turma["turma"] for turma in futebol_turmas]
        if not turmas:
            st.info("Nenhuma turma de futebol para este professor.")
            return
        turma_padrao = st.session_state.get("turma_selecionada", turmas[0])
        turma = st.selectbox("Turma", turmas, index=turmas.index(turma_padrao) if turma_padrao in turmas else 0)
        chamada_turma(turma)


def gestao_matriculas():
    st.header("Gestao de matriculas")
    subpagina = botoes_submenu("Gestao de matriculas")

    if subpagina == "Inscricoes":
        tabela_fechada("Inscricoes recebidas", ALUNOS)
    elif subpagina == "Incluir em turma":
        aluno = st.selectbox("Aluno", [item["nome"] for item in ALUNOS])
        turma = st.selectbox("Turma", [item["turma"] for item in TURMAS])
        if st.button("Incluir aluno na turma"):
            st.success(f"{aluno} incluido em {turma} para demonstracao.")
    elif subpagina == "Pendencias":
        tabela_fechada("Pendencias de matricula", [item for item in ALUNOS if item["status"] == "Pendente"])


def digitalizacao():
    st.header("Digitalizacao")
    subpagina = botoes_submenu("Digitalizacao")

    if subpagina == "Enviar ficha":
        st.file_uploader("Enviar ficha digitalizada", type=["pdf", "png", "jpg", "jpeg"])
        st.info("Nesta versao, o envio e demonstrativo. Depois podemos incluir OCR.")
    elif subpagina == "Revisar dados":
        tabela_fechada("Fichas para revisao", FICHAS)
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
        tabela_fechada("Dados das oficinas", TURMAS)
    elif subpagina == "Esportivo":
        st.subheader("Resumo esportivo")
        tabela_fechada("Jogos e resultados", JOGOS)


aplicar_estilo()
exibir_logo_sidebar()
perfil = st.sidebar.selectbox("Perfil", ["Professor", "Gestor", "Diretor"])
professores = sorted({turma["professor"] for turma in TURMAS})
professor = st.sidebar.selectbox("Professor demonstrativo", professores) if perfil == "Professor" else ""
if "query_params_aplicados" not in st.session_state:
    aplicar_query_params(perfil)
    st.session_state.query_params_aplicados = True
pagina = selecionar_pagina(perfil)

if pagina == "Inicio":
    inicio(perfil, professor)
elif pagina == "Alunos":
    alunos(perfil, professor)
elif pagina == "Oficinas":
    oficinas(perfil, professor)
elif pagina == "Agenda":
    agenda()
elif pagina == "Futebol":
    futebol(perfil, professor)
elif pagina == "Gestao de matriculas":
    gestao_matriculas()
elif pagina == "Digitalizacao":
    digitalizacao()
elif pagina == "Dashboard":
    dashboard()
