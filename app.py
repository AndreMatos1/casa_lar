import base64
from datetime import date
from html import escape
from pathlib import Path
from urllib.parse import urlencode
import streamlit as st


LOGO_PATH = Path(__file__).parent / "assets" / "logo.png"

st.set_page_config(
    page_title="Irmã Carmen Casa Lar",
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
        "oficina": "Danças",
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
        "oficina": "Danças",
        "modalidade": "Danças Urbanas",
        "turma": "Danças Urbanas I",
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
        "oficina": "Danças",
        "modalidade": "Ballet",
        "turma": "Ballet Infantil A",
        "professor": "Camila Rocha",
        "status": "Ativo",
    },
]


TURMAS = [
    {
        "oficina": "Danças",
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
        "oficina": "Danças",
        "modalidade": "Danças Urbanas",
        "turma": "Danças Urbanas I",
        "professor": "Camila Rocha",
        "dias": ["Terça", "Quinta"],
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
        "dias": ["Terça", "Quinta"],
        "horario": "15:30 - 17:00",
        "local": "Campo Principal",
        "vagas": 25,
        "matriculados": 21,
    },
    {
        "oficina": "Música",
        "modalidade": "Violão",
        "turma": "Violão Iniciante",
        "professor": "Marcos Araujo",
        "dias": ["Segunda"],
        "horario": "14:00 - 15:30",
        "local": "Sala de Música",
        "vagas": 15,
        "matriculados": 9,
    },
]


JOGOS = [
    {
        "categoria": "Sub-12",
        "turma": "Sub-12 Futebol",
        "competicao": "Liga Amistosa Regional",
        "data": "2026-06-20",
        "horario": "09:00",
        "local": "Campo Principal",
        "adversario": "Projeto Esperanca",
        "status": "Agendado",
        "placar": "-",
    },
    {
        "categoria": "Sub-14",
        "turma": "Sub-14 Futebol",
        "competicao": "Copa Solidariedade",
        "data": "2026-06-08",
        "horario": "15:00",
        "local": "Campo Principal",
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


USUARIOS_INICIAIS = [
    {
        "id": "USR-001",
        "nome": "Camila Rocha",
        "usuario": "camila.rocha",
        "senha": "123456",
        "email": "camila.rocha@casalar.org",
        "perfil": "Professor",
        "status": "Ativo",
        "vinculo": "Ballet e Danças Urbanas",
    },
    {
        "id": "USR-002",
        "nome": "Diego Martins",
        "usuario": "diego.martins",
        "senha": "123456",
        "email": "diego.martins@casalar.org",
        "perfil": "Professor",
        "status": "Ativo",
        "vinculo": "Futebol",
    },
    {
        "id": "USR-003",
        "nome": "Mariana Alves",
        "usuario": "mariana.alves",
        "senha": "123456",
        "email": "mariana.alves@casalar.org",
        "perfil": "Gestor",
        "status": "Ativo",
        "vinculo": "Secretaria",
    },
    {
        "id": "USR-004",
        "nome": "Irene Costa",
        "usuario": "irene.costa",
        "senha": "123456",
        "email": "irene.costa@casalar.org",
        "perfil": "Diretor",
        "status": "Ativo",
        "vinculo": "Diretoria",
    },
    {
        "id": "USR-005",
        "nome": "Andre Matos",
        "usuario": "andre.matos",
        "senha": "507@Dias",
        "email": "andre.matos@casalar.org",
        "perfil": "Gestor",
        "status": "Ativo",
        "vinculo": "Demonstração",
    },
]


DIAS_SEMANA = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
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
        "Usuarios",
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
        "Usuarios",
    ],
}


SUBMENUS = {
    "Alunos": ["Consulta", "Meus alunos", "Cadastro", "Pendencias"],
    "Oficinas": ["Agenda semanal", "Minhas turmas", "Chamada"],
    "Agenda": ["Aulas", "Jogos", "Treinos", "Recados"],
    "Futebol": ["Turmas", "Agenda jogo", "Agenda treinos", "Resultados", "Chamada"],
    "Gestao de matriculas": [
        "Cadastrar nova atividade",
        "Cadastrar novos alunos",
        "Criar novas turmas",
        "Pendencias",
        "Base de inscritos",
    ],
    "Digitalizacao": ["Enviar ficha", "Revisar dados", "Aprovar cadastro"],
    "Usuarios": ["Lista", "Cadastrar", "Editar", "Excluir"],
    "Dashboard": ["Indicadores", "Oficinas", "Esportivo"],
}


ROTULOS = {
    "Inicio": "Início",
    "Gestao de matriculas": "Gestão de cadastro",
    "Inscricoes": "Inscrições",
    "Pendencias": "Pendências",
    "Digitalizacao": "Digitalização",
    "Usuarios": "Usuários",
    "Agenda jogo": "Agenda de jogos",
    "Agenda treinos": "Agenda de treinos",
    "Meus alunos": "Meus alunos",
    "Minhas turmas": "Minhas turmas",
    "Cadastrar nova atividade": "Cadastrar nova atividade",
    "Cadastrar novos alunos": "Cadastrar novos alunos",
    "Criar novas turmas": "Criar novas turmas",
    "Base de inscritos": "Base de inscritos",
}


COLUNAS_EXIBICAO = {
    "id": "ID",
    "nome": "Nome",
    "idade": "Idade",
    "responsavel": "Responsável",
    "telefone": "Telefone",
    "oficina": "Oficina",
    "modalidade": "Modalidade",
    "turma": "Turma",
    "professor": "Professor",
    "status": "Status",
    "dias": "Dias",
    "horario": "Horário",
    "local": "Local",
    "vagas": "Vagas",
    "matriculados": "Matriculados",
    "categoria": "Categoria",
    "competicao": "Competição",
    "data": "Data",
    "adversario": "Adversário",
    "placar": "Placar",
    "arquivo": "Arquivo",
    "nome_detectado": "Nome detectado",
    "responsavel_detectado": "Responsável detectado",
    "confianca": "Confiança",
    "aluno": "Aluno",
    "observacao": "Observação",
    "usuario": "Usuário",
    "email": "E-mail",
    "perfil": "Perfil",
    "vinculo": "Vínculo",
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
        div.stFormSubmitButton > button {
            width: 100%;
            border-radius: 14px;
            border: 1px solid #1d4ed8;
            background: linear-gradient(180deg, #2563eb 0%, #1d4ed8 100%);
            color: #ffffff;
            font-weight: 700;
            min-height: 42px;
            padding: 0.62rem 0.9rem;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.24);
        }
        div.stFormSubmitButton > button:hover {
            border-color: #1746a2;
            background: #1746a2;
            color: #ffffff;
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
        .login-logo-wrap {
            text-align: center;
            margin-bottom: 12px;
        }
        .login-logo {
            width: min(460px, 100%);
            max-height: 250px;
            object-fit: contain;
        }
        .login-title {
            text-align: center;
            color: #0f172a;
            font-size: 1.7rem;
            font-weight: 800;
            margin: 16px 0 8px 0;
        }
        .login-subtitle {
            text-align: center;
            color: #667085;
            font-size: 0.95rem;
            margin-bottom: 28px;
        }
        .login-spacer {
            height: 28px;
        }
        .login-divider {
            height: 1px;
            background: #d0d5dd;
            margin: 0 0 28px 0;
        }
        .grid-caption {
            color: #475467;
            font-size: 0.92rem;
            margin: 0.25rem 0 0.75rem 0;
        }
        .table-header {
            border: 1px solid #d9e2ec;
            border-radius: 12px 12px 0 0;
            background: #f8fafc;
            padding: 10px 12px;
            font-weight: 800;
        }
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.student-grid-row) {
            border-color: #d9e2ec;
            border-radius: 0;
            box-shadow: none;
        }
        .student-grid-row {
            min-height: 42px;
            display: flex;
            align-items: center;
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
        .agenda-grid {
            display: grid;
            grid-template-columns: repeat(6, minmax(130px, 1fr));
            border: 1px solid #d9e2ec;
            border-radius: 14px;
            overflow-x: auto;
            background: #ffffff;
            box-shadow: 0 1px 3px rgba(16, 24, 40, 0.08);
        }
        .agenda-day {
            min-height: 316px;
            padding: 10px;
            border-right: 1px solid #e5edf5;
            border-bottom: 1px solid #e5edf5;
            border-radius: 0;
            background:
                linear-gradient(#eef3f8 1px, transparent 1px),
                linear-gradient(90deg, #f3f6fa 1px, transparent 1px),
                #ffffff;
            background-size: 100% 56px, 56px 100%, 100% 100%;
            box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.9);
        }
        .agenda-day.today {
            border-color: #2563eb;
            background:
                linear-gradient(#dceafe 1px, transparent 1px),
                linear-gradient(90deg, #e7efff 1px, transparent 1px),
                #f8fbff;
            background-size: 100% 56px, 56px 100%, 100% 100%;
        }
        .agenda-day .card {
            margin-bottom: 10px;
        }
        .agenda-event {
            display: block;
            min-height: 76px;
            margin-top: 10px;
            padding: 12px;
            border: 1px solid #d9e2ec;
            border-radius: 10px;
            background: rgba(248, 250, 252, 0.92);
            color: #0f172a !important;
            text-align: center;
            text-decoration: none !important;
            box-shadow: 0 1px 2px rgba(16, 24, 40, 0.06);
        }
        .agenda-event:hover {
            border-color: #2563eb;
            background: #edf4ff;
        }
        .agenda-slot {
            min-height: 76px;
            padding: 12px;
            border: 1px solid #d9e2ec;
            border-radius: 10px;
            background: rgba(248, 250, 252, 0.92);
            text-align: center;
            box-shadow: 0 1px 2px rgba(16, 24, 40, 0.06);
        }
        .agenda-empty {
            color: #98a2b3;
            font-size: 0.9rem;
            padding: 12px 2px;
        }
        @media (max-width: 900px) {
            .agenda-grid {
                grid-template-columns: repeat(6, minmax(190px, 1fr));
            }
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
        left, center, right = st.sidebar.columns([1, 3, 1])
        center.image(str(LOGO_PATH), width=130)


def exibir_logo_inicio():
    if LOGO_PATH.exists():
        left, center, right = st.columns([1, 1, 1])
        center.image(str(LOGO_PATH), width=360)


def imagem_base64(caminho):
    return base64.b64encode(caminho.read_bytes()).decode("utf-8")


def exibir_logo_login():
    if LOGO_PATH.exists():
        st.markdown(
            f"""
            <div class="login-logo-wrap">
                <img class="login-logo" src="data:image/png;base64,{imagem_base64(LOGO_PATH)}" alt="Casa Lar">
            </div>
            """,
            unsafe_allow_html=True,
        )


def usuario_para_login(valor):
    return (valor or "").strip().lower()


def autenticar_usuario(usuario, senha):
    usuario_normalizado = usuario_para_login(usuario)
    for item in st.session_state.usuarios:
        login = usuario_para_login(item.get("usuario") or item.get("email"))
        email = usuario_para_login(item.get("email"))
        if usuario_normalizado in {login, email} and senha == item.get("senha") and item["status"] == "Ativo":
            return item
    return None


def entrar(usuario):
    st.session_state.usuario_logado = usuario.copy()
    st.session_state.pagina = MENU_POR_PERFIL[usuario["perfil"]][0]
    for chave in ["page", "sub", "turma", "aluno"]:
        if chave in st.query_params:
            del st.query_params[chave]


def sair():
    for chave in ["usuario_logado", "pagina", "turma_selecionada", "aluno_selecionado"]:
        if chave in st.session_state:
            del st.session_state[chave]
    for chave in ["page", "sub", "turma", "aluno"]:
        if chave in st.query_params:
            del st.query_params[chave]


def tela_login():
    st.markdown("<div class='login-spacer'></div>", unsafe_allow_html=True)
    left, center, right = st.columns([1, 1.25, 1])
    with center:
        exibir_logo_login()
        st.markdown(
            """
            <div class="login-title">Acesso ao Sistema</div>
            <div class="login-subtitle">Informe seu usuário e senha para continuar</div>
            <div class="login-divider"></div>
            """,
            unsafe_allow_html=True,
        )
        with st.form("login"):
            usuario = st.text_input("Usuário", placeholder="Seu usuário")
            senha = st.text_input("Senha", type="password", placeholder="Sua senha")
            with st.expander("Esqueci minha senha", expanded=False):
                st.caption("Neste protótipo, solicite a redefinição para um gestor do sistema.")
            acessar = st.form_submit_button("Entrar", use_container_width=True)

        if acessar:
            usuario_encontrado = autenticar_usuario(usuario, senha)
            if usuario_encontrado:
                entrar(usuario_encontrado)
                st.rerun()
            st.error("Usuário ou senha inválidos, ou usuário inativo.")


def navegar_para(pagina, subpagina=None, turma=None):
    st.session_state.pagina = pagina
    if subpagina:
        st.session_state[f"subpagina_{pagina}"] = subpagina
    if turma:
        st.session_state.turma_selecionada = turma


def abrir_cadastro_aluno(aluno_id):
    st.session_state.pagina = "Alunos"
    st.session_state.subpagina_Alunos = "Cadastro"
    st.session_state.aluno_selecionado = aluno_id


def nav_link(label, pagina, subpagina=None, turma=None, active=False, sidebar=False, key_suffix=""):
    key = f"nav_{'side' if sidebar else 'main'}_{label}_{pagina}_{subpagina}_{turma}_{key_suffix}"
    st.button(
        ROTULOS.get(label, label),
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
    aluno = params.get("aluno")
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
    if aluno:
        st.session_state.aluno_selecionado = aluno


def selecionar_pagina(perfil):
    paginas = MENU_POR_PERFIL[perfil]
    if "pagina" not in st.session_state or st.session_state.pagina not in paginas:
        st.session_state.pagina = paginas[0]

    st.sidebar.title("Casa Lar")
    usuario = st.session_state.get("usuario_logado", {})
    st.sidebar.caption(f"{usuario.get('nome', '')} | {perfil}")
    if st.sidebar.button("Sair", key="logout", use_container_width=True):
        sair()
        st.rerun()
    st.sidebar.divider()
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


def formatar_data_br(valor):
    if not valor:
        return valor
    texto = str(valor)
    try:
        if len(texto) == 10 and texto[4] == "-" and texto[7] == "-":
            ano, mes, dia = texto.split("-")
            return f"{dia}/{mes}/{ano}"
    except ValueError:
        return valor
    return valor


def dados_para_exibicao(dados):
    exibicao = []
    for item in dados:
        novo = {}
        for chave, valor in item.items():
            rotulo = COLUNAS_EXIBICAO.get(chave, chave)
            novo[rotulo] = formatar_data_br(valor) if chave == "data" else valor
        exibicao.append(novo)
    return exibicao


def tabela_fechada(titulo, dados):
    with st.expander(titulo, expanded=False):
        st.dataframe(dados_para_exibicao(dados), use_container_width=True, hide_index=True)


def status_cadastro_aluno(aluno):
    if aluno["status"] == "Pendente":
        return "Com pendência"
    return "Completo"


def pendencia_aluno(aluno):
    if aluno["status"] != "Pendente":
        return "-"
    return aluno.get("observacoes") or "Cadastro pendente"


def lista_alunos_com_acesso(titulo, alunos):
    st.subheader(titulo)
    if not alunos:
        st.info("Nenhum aluno encontrado.")
        return

    with st.container(border=True):
        cabecalho = st.columns([2.4, 1.6, 1.3, 2.2, 1.4])
        cabecalho[0].markdown("**Aluno**")
        cabecalho[1].markdown("**Turma**")
        cabecalho[2].markdown("**Status**")
        cabecalho[3].markdown("**Pendência**")
        cabecalho[4].markdown("**Cadastro**")

    for indice, aluno in enumerate(alunos):
        with st.container(border=True):
            linha = st.columns([2.4, 1.6, 1.3, 2.2, 1.4])
            linha[0].markdown(f"<div class='student-grid-row'>{escape(aluno['nome'])}</div>", unsafe_allow_html=True)
            linha[1].markdown(f"<div class='student-grid-row'>{escape(aluno['turma'])}</div>", unsafe_allow_html=True)
            linha[2].markdown(
                f"<div class='student-grid-row'>{escape(status_cadastro_aluno(aluno))}</div>",
                unsafe_allow_html=True,
            )
            linha[3].markdown(
                f"<div class='student-grid-row'>{escape(pendencia_aluno(aluno))}</div>",
                unsafe_allow_html=True,
            )
            linha[4].button(
                "Abrir cadastro",
                key=f"abrir_cadastro_{titulo}_{aluno['id']}_{indice}",
                use_container_width=True,
                on_click=abrir_cadastro_aluno,
                args=(aluno["id"],),
            )


def inicializar_usuarios():
    if "usuarios" not in st.session_state:
        st.session_state.usuarios = [usuario.copy() for usuario in USUARIOS_INICIAIS]
    for usuario in st.session_state.usuarios:
        usuario.setdefault("usuario", usuario_para_login(usuario.get("email", "").split("@")[0]))
        usuario.setdefault("senha", "123456")
    if not any(usuario.get("usuario") == "andre.matos" for usuario in st.session_state.usuarios):
        st.session_state.usuarios.append(USUARIOS_INICIAIS[-1].copy())


def inicializar_jogos():
    if "jogos" not in st.session_state:
        st.session_state.jogos = [jogo.copy() for jogo in JOGOS]


def usuarios_para_exibicao(usuarios):
    return [{chave: valor for chave, valor in usuario.items() if chave != "senha"} for usuario in usuarios]


def proximo_id_usuario():
    numeros = []
    for usuario in st.session_state.usuarios:
        try:
            numeros.append(int(usuario["id"].split("-")[1]))
        except (IndexError, ValueError):
            continue
    return f"USR-{max(numeros, default=0) + 1:03d}"


def alunos_por_turma(turma):
    return [aluno for aluno in ALUNOS if aluno["turma"] == turma]


def turmas_do_professor(professor):
    return [turma for turma in TURMAS if turma["professor"] == professor]


def alunos_do_professor(professor):
    return [aluno for aluno in ALUNOS if aluno["professor"] == professor]


def jogos_salvos():
    return st.session_state.get("jogos", JOGOS)


def jogos_para_tabela():
    return jogos_salvos()


def pdf_escape(texto):
    return str(texto).replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def gerar_pdf_convocacao(jogo, turma, convocados):
    linhas = [
        "Casa Lar - Associação Irmã Carmen",
        "Convocação de Jogadores",
        "",
        f"Turma: {turma['turma']}",
        f"Categoria: {jogo['categoria']}",
        f"Competição: {jogo['competicao']}",
        f"Adversário: {jogo['adversario']}",
        f"Data: {formatar_data_br(jogo['data'])}",
        f"Horário: {jogo.get('horario', '-')}",
        f"Local: {jogo.get('local', '-')}",
        "",
        "Jogadores convocados:",
    ]
    linhas.extend([f"- {aluno}" for aluno in convocados])
    if not convocados:
        linhas.append("- Nenhum jogador selecionado")

    comandos = ["BT", "/F1 12 Tf", "50 790 Td", "16 TL"]
    for linha in linhas:
        comandos.append(f"({pdf_escape(linha)}) Tj")
        comandos.append("T*")
    comandos.append("ET")
    conteudo = "\n".join(comandos).encode("latin-1", "replace")

    objetos = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
        b"<< /Length " + str(len(conteudo)).encode("ascii") + b" >>\nstream\n" + conteudo + b"\nendstream",
    ]
    pdf = bytearray(b"%PDF-1.4\n")
    offsets = [0]
    for indice, objeto in enumerate(objetos, start=1):
        offsets.append(len(pdf))
        pdf.extend(f"{indice} 0 obj\n".encode("ascii"))
        pdf.extend(objeto)
        pdf.extend(b"\nendobj\n")
    inicio_xref = len(pdf)
    pdf.extend(f"xref\n0 {len(objetos) + 1}\n".encode("ascii"))
    pdf.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        pdf.extend(f"{offset:010d} 00000 n \n".encode("ascii"))
    pdf.extend(
        f"trailer\n<< /Size {len(objetos) + 1} /Root 1 0 R >>\nstartxref\n{inicio_xref}\n%%EOF".encode(
            "ascii"
        )
    )
    return bytes(pdf)


def formulario_cadastro_aluno(form_key="cadastro_aluno", aluno=None):
    if aluno:
        st.subheader(f"Cadastro de {aluno['nome']}")
        col1, col2, col3 = st.columns(3)
        col1.metric("Status do cadastro", status_cadastro_aluno(aluno))
        col2.metric("Turma", aluno["turma"])
        col3.metric("Idade", aluno["idade"])

        st.write(f"**Responsável:** {aluno['responsavel']}")
        st.write(f"**Telefone:** {aluno['telefone']}")
        st.write(f"**Pendência:** {pendencia_aluno(aluno)}")

        with st.expander("Dados do cadastro", expanded=True):
            st.text_input("Nome da criança", value=aluno["nome"], key=f"{form_key}_nome")
            st.text_input("Responsável", value=aluno["responsavel"], key=f"{form_key}_responsavel")
            st.text_input("WhatsApp", value=aluno["telefone"], key=f"{form_key}_telefone")
            st.text_input("Turma", value=aluno["turma"], key=f"{form_key}_turma")
            opcoes_status = ["Ativo", "Pendente", "Inativo"]
            st.selectbox(
                "Status da matrícula",
                opcoes_status,
                index=opcoes_status.index(aluno["status"]) if aluno["status"] in opcoes_status else 0,
                key=f"{form_key}_status",
            )
            st.text_area("Observações", value=aluno.get("observacoes", ""), key=f"{form_key}_obs")
            st.file_uploader(
                "Enviar documento deste aluno",
                type=["pdf", "png", "jpg", "jpeg"],
                key=f"{form_key}_upload",
            )
            if st.button("Salvar alterações de teste", key=f"{form_key}_salvar"):
                st.success(f"Cadastro de {aluno['nome']} atualizado para demonstração.")
        return

    with st.form(form_key):
        col1, col2 = st.columns(2)
        nome = col1.text_input("Nome da criança")
        responsavel = col2.text_input("Responsável")
        telefone = col1.text_input("WhatsApp")
        idade = col2.number_input("Idade", min_value=0, max_value=18, value=8)
        turma = col1.selectbox("Turma", [item["turma"] for item in TURMAS])
        status = col2.selectbox("Status da matrícula", ["Ativo", "Pendente", "Inativo"])
        observacoes = st.text_area("Observações")
        enviar = st.form_submit_button("Cadastrar aluno")
    if enviar:
        if not nome or not responsavel:
            st.error("Informe o nome da criança e o responsável.")
        else:
            st.success(f"Cadastro de {nome} registrado para teste.")
            if observacoes:
                st.caption(f"Observações: {observacoes}")


def metricas():
    ativos = len([aluno for aluno in ALUNOS if aluno["status"] == "Ativo"])
    pendentes = len([aluno for aluno in ALUNOS if aluno["status"] == "Pendente"])
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Alunos ativos", ativos)
    col2.metric("Cadastros pendentes", pendentes)
    col3.metric("Turmas", len(TURMAS))
    col4.metric("Jogos", len(jogos_salvos()))


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
    colunas_html = []
    for dia in DIAS_SEMANA:
        eventos = [turma for turma in turmas if dia in turma["dias"]]
        classe = "agenda-day today" if dia == DIA_ATUAL_DEMO else "agenda-day"
        eventos_html = []
        if not eventos:
            eventos_html.append("<div class='agenda-empty'>Sem atividades</div>")
        for turma in eventos:
            subpagina = "Minhas turmas" if destino == "Oficinas" else "Turmas"
            href = "?" + urlencode({"page": destino, "sub": subpagina, "turma": turma["turma"]})
            eventos_html.append(
                "<a class='agenda-event' href='{href}' target='_self'>"
                "<span>{horario} | {turma}</span>"
                "</a>".format(
                    href=escape(href, quote=True),
                    horario=escape(turma["horario"]),
                    turma=escape(turma["turma"]),
                )
            )
        colunas_html.append(
            "<div class='{classe}'>"
            "<div class='card {today_card}'><strong>{dia}</strong><br>"
            "<span class='muted'>{rotulo}</span></div>"
            "{eventos}"
            "</div>".format(
                classe=classe,
                today_card="today-card" if dia == DIA_ATUAL_DEMO else "",
                dia=escape(dia),
                rotulo="Hoje" if dia == DIA_ATUAL_DEMO else "Semana",
                eventos="".join(eventos_html),
            )
        )
    st.markdown(
        "<div class='agenda-grid'>{}</div>".format("".join(colunas_html)),
        unsafe_allow_html=True,
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
        data_chamada = st.date_input("Data da chamada", value=date.today(), format="DD/MM/YYYY")
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
    st.title("Irmã Carmen Casa Lar")
    st.caption("Protótipo inicial em Streamlit com foco na rotina de professores, gestores e diretores.")
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
            busca = st.text_input("Buscar aluno, responsável, turma ou oficina")
            buscar = st.form_submit_button("Buscar")
        filtrados = base
        if buscar and busca:
            termo = busca.lower()
            filtrados = [aluno for aluno in base if termo in str(aluno).lower()]
        lista_alunos_com_acesso("Resultado da consulta", filtrados)

    elif subpagina == "Meus alunos":
        st.caption("Alunos vinculados às turmas do professor selecionado.")
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
        lista_alunos_com_acesso("Meus alunos", filtrados)
        if filtro_turma != "Todas":
            nav_link(
                "Abrir turma selecionada",
                "Oficinas",
                "Minhas turmas",
                filtro_turma,
                key_suffix="meus_alunos",
            )

    elif subpagina == "Cadastro":
        aluno_id = st.session_state.get("aluno_selecionado")
        aluno = next((item for item in base if item["id"] == aluno_id), None)
        if aluno_id and not aluno:
            st.warning("Aluno selecionado não encontrado para este perfil.")
        formulario_cadastro_aluno("cadastro_aluno", aluno)

    elif subpagina == "Pendencias":
        pendentes = [item for item in base if item["status"] == "Pendente"]
        lista_alunos_com_acesso("Pendências dos alunos", pendentes)
        tabela_fechada("Fichas pendentes de revisão", FICHAS)


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
        tabela_fechada("Agenda de jogos", jogos_para_tabela())
    elif subpagina == "Treinos":
        treinos = [turma for turma in TURMAS if turma["modalidade"] == "Futebol"]
        agenda_semanal(treinos, "Futebol")
    elif subpagina == "Recados":
        st.selectbox("Aluno", [item["nome"] for item in ALUNOS])
        st.text_area("Mensagem", "Ola, temos um comunicado da Casa Lar sobre a proxima atividade.")
        st.button("Simular envio por WhatsApp")
        st.info("Na versão real, podemos integrar WhatsApp Cloud API, Twilio, Z-API ou outro provedor.")


def futebol(perfil, professor):
    st.header("Futebol")
    subpagina = botoes_submenu("Futebol")
    futebol_turmas = [item for item in TURMAS if item["modalidade"] == "Futebol"]
    if perfil == "Professor":
        futebol_turmas = [item for item in futebol_turmas if item["professor"] == professor]
    if not futebol_turmas:
        st.info("Nenhuma turma de futebol disponível para este perfil.")
        return

    if subpagina == "Turmas":
        cols = st.columns(2)
        for index, turma in enumerate(futebol_turmas):
            with cols[index % 2]:
                card_turma(turma, "Futebol", "Turmas", key_suffix=f"futebol_{index}")
        selecionada = st.session_state.get(
            "turma_selecionada",
            futebol_turmas[0]["turma"] if futebol_turmas else "",
        )
        if selecionada:
            turma = next((item for item in futebol_turmas if item["turma"] == selecionada), None)
            if turma:
                st.divider()
                st.subheader(f"Detalhes da turma: {selecionada}")
                col1, col2, col3 = st.columns(3)
                col1.metric("Vagas", turma["vagas"])
                col2.metric("Matriculados", turma["matriculados"])
                col3.metric("Alunos na amostra", len(alunos_por_turma(selecionada)))
                lista_alunos_com_acesso("Jogadores da turma", alunos_por_turma(selecionada))

    elif subpagina == "Agenda jogo":
        aba_agenda, aba_novo, aba_convocar = st.tabs(
            ["Agenda de jogos", "Novo agendamento", "Convocar jogadores"]
        )
        with aba_agenda:
            tabela_fechada("Jogos cadastrados", jogos_para_tabela())

        with aba_novo:
            with st.form("novo_jogo"):
                col1, col2 = st.columns(2)
                turma_nome = col1.selectbox("Turma", [turma["turma"] for turma in futebol_turmas])
                data_jogo = col2.date_input("Data do jogo", value=date.today(), format="DD/MM/YYYY")
                horario = col1.text_input("Horário", placeholder="Ex.: 09:00")
                local = col2.text_input("Local", placeholder="Ex.: Campo Principal")
                competicao = col1.text_input("Competição")
                adversario = col2.text_input("Adversário")
                salvar = st.form_submit_button("Salvar agendamento")
            if salvar:
                if not competicao or not adversario or not horario:
                    st.error("Informe competição, adversário e horário.")
                else:
                    st.session_state.jogos.append(
                        {
                            "categoria": turma_nome.replace(" Futebol", ""),
                            "turma": turma_nome,
                            "competicao": competicao,
                            "data": data_jogo.isoformat(),
                            "horario": horario,
                            "local": local or "A definir",
                            "adversario": adversario,
                            "status": "Agendado",
                            "placar": "-",
                        }
                    )
                    st.success("Agendamento incluído para demonstração.")

        with aba_convocar:
            jogos_agendados = [jogo for jogo in jogos_salvos() if jogo["status"] == "Agendado"]
            if not jogos_agendados:
                st.info("Nenhum jogo agendado disponível para convocação.")
            else:
                jogo_index = st.selectbox(
                    "Jogo",
                    range(len(jogos_agendados)),
                    format_func=lambda indice: (
                        f"{formatar_data_br(jogos_agendados[indice]['data'])} | "
                        f"{jogos_agendados[indice].get('horario', '-')} | "
                        f"{jogos_agendados[indice]['turma']} x {jogos_agendados[indice]['adversario']}"
                    ),
                )
                jogo = jogos_agendados[jogo_index]
                turma = next((item for item in futebol_turmas if item["turma"] == jogo["turma"]), None)
                if not turma:
                    st.warning("Turma do jogo não encontrada para este perfil.")
                else:
                    alunos = alunos_por_turma(turma["turma"])
                    st.caption("Marque os jogadores convocados para gerar o PDF.")
                    cabecalho = st.columns([3, 1.2, 2])
                    cabecalho[0].markdown("**Jogador**")
                    cabecalho[1].markdown("**Convocar**")
                    cabecalho[2].markdown("**Turma**")
                    convocados = []
                    for aluno in alunos:
                        linha = st.columns([3, 1.2, 2])
                        linha[0].write(aluno["nome"])
                        convocar = linha[1].checkbox(
                            "Convocar",
                            value=True,
                            key=f"convocar_{jogo['data']}_{jogo['turma']}_{aluno['id']}",
                            label_visibility="collapsed",
                        )
                        linha[2].write(aluno["turma"])
                        if convocar:
                            convocados.append(aluno["nome"])
                    pdf = gerar_pdf_convocacao(jogo, turma, convocados)
                    st.download_button(
                        "Baixar PDF da convocação",
                        data=pdf,
                        file_name=f"convocacao_{jogo['turma'].lower().replace(' ', '_')}.pdf",
                        mime="application/pdf",
                        use_container_width=True,
                    )

    elif subpagina == "Agenda treinos":
        agenda_semanal(futebol_turmas, "Futebol")

    elif subpagina == "Resultados":
        tabela_fechada("Resultados", [item for item in jogos_salvos() if item["status"] == "Finalizado"])
        st.subheader("Registrar resultado demonstrativo")
        jogo = st.selectbox("Jogo", [f"{item['categoria']} - {item['adversario']}" for item in jogos_salvos()])
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
    st.header("Gestão de cadastro")
    subpagina = botoes_submenu("Gestao de matriculas")

    if subpagina == "Cadastrar nova atividade":
        with st.form("cadastro_atividade"):
            col1, col2 = st.columns(2)
            oficina = col1.text_input("Oficina", placeholder="Ex.: Esportes, Música, Danças")
            modalidade = col2.text_input("Atividade", placeholder="Ex.: Futebol, Violão, Ballet")
            responsavel = col1.text_input("Professor ou responsável")
            local = col2.text_input("Local")
            descricao = st.text_area("Observações da atividade")
            salvar = st.form_submit_button("Cadastrar atividade")
        if salvar:
            if not oficina or not modalidade:
                st.error("Informe a oficina e a atividade.")
            else:
                st.success(f"Atividade {modalidade} cadastrada para demonstração.")
                if descricao:
                    st.caption(descricao)

    elif subpagina == "Cadastrar novos alunos":
        formulario_cadastro_aluno("cadastro_aluno_matriculas")

    elif subpagina == "Criar novas turmas":
        with st.form("cadastro_turma"):
            col1, col2 = st.columns(2)
            nome_turma = col1.text_input("Nome da turma")
            modalidade = col2.selectbox("Atividade", sorted({item["modalidade"] for item in TURMAS}))
            professor = col1.selectbox("Professor", sorted({item["professor"] for item in TURMAS}))
            vagas = col2.number_input("Vagas", min_value=1, max_value=80, value=20)
            dias = st.multiselect("Dias da semana", DIAS_SEMANA)
            horario = col1.text_input("Horário", placeholder="Ex.: 09:00 - 10:15")
            local = col2.text_input("Local")
            salvar = st.form_submit_button("Criar turma")
        if salvar:
            if not nome_turma or not dias or not horario:
                st.error("Informe nome, dias e horário da turma.")
            else:
                st.success(f"Turma {nome_turma} criada para demonstração.")

    elif subpagina == "Pendencias":
        lista_alunos_com_acesso(
            "Pendências de cadastro",
            [item for item in ALUNOS if item["status"] == "Pendente"],
        )

    elif subpagina == "Base de inscritos":
        st.caption("Consulta geral da base demonstrativa, incluindo alunos ativos, pendentes e inativos.")
        lista_alunos_com_acesso("Base de inscritos", ALUNOS)


def digitalizacao():
    st.header("Digitalização")
    subpagina = botoes_submenu("Digitalizacao")

    if subpagina == "Enviar ficha":
        st.file_uploader("Enviar ficha digitalizada", type=["pdf", "png", "jpg", "jpeg"])
        st.info("Nesta versão, o envio é demonstrativo. Depois podemos incluir OCR.")
    elif subpagina == "Revisar dados":
        tabela_fechada("Fichas para revisão", FICHAS)
        st.text_input("Nome revisado")
        st.text_input("Responsável revisado")
    elif subpagina == "Aprovar cadastro":
        ficha = st.selectbox("Ficha para aprovar", [item["arquivo"] for item in FICHAS])
        if st.button("Aprovar ficha de teste"):
            st.success(f"Ficha {ficha} aprovada para cadastro.")


def usuarios():
    inicializar_usuarios()
    st.header("Gestão de usuários")
    subpagina = botoes_submenu("Usuarios")

    if subpagina == "Lista":
        busca = st.text_input("Buscar por nome, e-mail, perfil ou vínculo")
        usuarios_filtrados = st.session_state.usuarios
        if busca:
            termo = busca.lower()
            usuarios_filtrados = [
                usuario for usuario in usuarios_filtrados if termo in str(usuario).lower()
            ]
        st.dataframe(
            dados_para_exibicao(usuarios_para_exibicao(usuarios_filtrados)),
            use_container_width=True,
            hide_index=True,
        )

    elif subpagina == "Cadastrar":
        with st.form("form_cadastrar_usuario"):
            col1, col2 = st.columns(2)
            nome = col1.text_input("Nome")
            usuario_login = col2.text_input("Usuário", placeholder="Ex.: nome.sobrenome")
            email = col1.text_input("E-mail")
            senha_temp = col2.text_input("Senha temporária", type="password")
            perfil_usuario = col1.selectbox("Perfil", ["Professor", "Gestor", "Diretor"])
            status_usuario = col2.selectbox("Status", ["Ativo", "Inativo"])
            vinculo = st.text_input("Vínculo ou área", placeholder="Ex.: Futebol, Ballet, Secretaria")
            salvar = st.form_submit_button("Cadastrar usuário")
        if salvar:
            if not nome or not usuario_login or not senha_temp:
                st.error("Informe nome, usuário e senha temporária para cadastrar o usuário.")
            elif any(
                usuario_para_login(usuario.get("usuario")) == usuario_para_login(usuario_login)
                for usuario in st.session_state.usuarios
            ):
                st.error("Já existe um usuário com este login.")
            else:
                st.session_state.usuarios.append(
                    {
                        "id": proximo_id_usuario(),
                        "nome": nome,
                        "usuario": usuario_para_login(usuario_login),
                        "senha": senha_temp,
                        "email": email,
                        "perfil": perfil_usuario,
                        "status": status_usuario,
                        "vinculo": vinculo,
                    }
                )
                st.success(f"Usuário {nome} cadastrado para teste.")

    elif subpagina == "Editar":
        if not st.session_state.usuarios:
            st.info("Nenhum usuário cadastrado.")
            return
        usuario_id = st.selectbox(
            "Usuário",
            [usuario["id"] for usuario in st.session_state.usuarios],
            format_func=lambda item_id: next(
                usuario["nome"] for usuario in st.session_state.usuarios if usuario["id"] == item_id
            ),
        )
        atual = next(usuario for usuario in st.session_state.usuarios if usuario["id"] == usuario_id)
        with st.form("form_editar_usuario"):
            col1, col2 = st.columns(2)
            nome = col1.text_input("Nome", value=atual["nome"])
            usuario_login = col2.text_input("Usuário", value=atual.get("usuario", ""))
            email = col1.text_input("E-mail", value=atual["email"])
            nova_senha = col2.text_input("Nova senha", type="password", placeholder="Manter senha atual")
            perfil_usuario = col1.selectbox(
                "Perfil",
                ["Professor", "Gestor", "Diretor"],
                index=["Professor", "Gestor", "Diretor"].index(atual["perfil"]),
            )
            status_usuario = col2.selectbox(
                "Status",
                ["Ativo", "Inativo"],
                index=["Ativo", "Inativo"].index(atual["status"]),
            )
            vinculo = st.text_input("Vínculo ou área", value=atual["vinculo"])
            salvar = st.form_submit_button("Salvar alterações")
        if salvar:
            atual.update(
                {
                    "nome": nome,
                    "usuario": usuario_para_login(usuario_login),
                    "email": email,
                    "perfil": perfil_usuario,
                    "status": status_usuario,
                    "vinculo": vinculo,
                }
            )
            if nova_senha:
                atual["senha"] = nova_senha
            if st.session_state.get("usuario_logado", {}).get("id") == atual["id"]:
                st.session_state.usuario_logado = atual.copy()
            st.success("Usuário atualizado para teste.")

    elif subpagina == "Excluir":
        if not st.session_state.usuarios:
            st.info("Nenhum usuário cadastrado.")
            return
        usuario_id = st.selectbox(
            "Usuário para excluir",
            [usuario["id"] for usuario in st.session_state.usuarios],
            format_func=lambda item_id: next(
                usuario["nome"] for usuario in st.session_state.usuarios if usuario["id"] == item_id
            ),
        )
        atual = next(usuario for usuario in st.session_state.usuarios if usuario["id"] == usuario_id)
        st.warning(f"Esta ação removerá {atual['nome']} da lista desta sessão de teste.")
        confirmar = st.checkbox("Confirmo a exclusão deste usuário")
        if confirmar:
            if st.button("Excluir usuário"):
                st.session_state.usuarios = [
                    usuario for usuario in st.session_state.usuarios if usuario["id"] != usuario_id
                ]
                st.success("Usuário excluído da sessão de teste.")
        else:
            st.info("Marque a confirmação para liberar o botão de exclusão.")


def dashboard():
    st.header("Dashboard da direção")
    subpagina = botoes_submenu("Dashboard")

    if subpagina == "Indicadores":
        metricas()
        st.subheader("Alunos por status")
        status = {}
        for aluno in ALUNOS:
            status[aluno["status"]] = status.get(aluno["status"], 0) + 1
        st.bar_chart(status)
    elif subpagina == "Oficinas":
        st.subheader("Matrículas por turma")
        st.bar_chart({turma["turma"]: turma["matriculados"] for turma in TURMAS})
        tabela_fechada("Dados das oficinas", TURMAS)
    elif subpagina == "Esportivo":
        st.subheader("Resumo esportivo")
        tabela_fechada("Jogos e resultados", jogos_para_tabela())


aplicar_estilo()
inicializar_usuarios()
inicializar_jogos()
if "usuario_logado" not in st.session_state:
    tela_login()
    st.stop()

exibir_logo_sidebar()
usuario_logado = st.session_state.usuario_logado
perfil = usuario_logado["perfil"]
professores = sorted({turma["professor"] for turma in TURMAS})
professor = ""
if perfil == "Professor":
    professor = usuario_logado["nome"] if usuario_logado["nome"] in professores else professores[0]
aplicar_query_params(perfil)
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
elif pagina == "Usuarios":
    usuarios()
elif pagina == "Dashboard":
    dashboard()
