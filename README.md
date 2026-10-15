# Casa Lar

Aplicação de demonstração da Associação Irmã Carmen Casa Lar, desenvolvida com Streamlit.

## Desenvolver no GitHub Codespaces

1. Abra o repositório [AndreMatos1/casa_lar](https://github.com/AndreMatos1/casa_lar) no GitHub.
2. Selecione **Code** > **Codespaces** > **Create codespace**. Escolha a branch que deseja desenvolver.
3. Na criação do ambiente, o Codespaces instala automaticamente as dependências de `requirements.txt`.
4. No terminal integrado, inicie a aplicação:

   ```bash
   python -m streamlit run app.py --server.address 0.0.0.0 --server.port 8501
   ```

5. Abra a aba **Ports** do Codespaces e acesse a porta `8501` (ela é encaminhada automaticamente).

## Executar localmente

Requer Python 3.12 ou compatível com as dependências do projeto.

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Salvar alterações no GitHub

Crie uma branch para cada conjunto de alterações. No terminal do Codespaces:

```bash
git switch -c minha-branch
git status
git add README.md app.py
git commit -m "Descreve as alterações"
git push -u origin minha-branch
```

Adapte a lista de arquivos no `git add` ao que você alterou. Depois, abra um Pull Request da sua branch para `main` no GitHub.

## Dependências

As bibliotecas Python usadas pela aplicação estão listadas em [`requirements.txt`](requirements.txt). O Codespaces as instala durante a criação do ambiente por meio da configuração em `.devcontainer/devcontainer.json`.

## Arquivos locais e segurança

O diretório `data/` é reservado a arquivos de dados locais e fica fora do controle do Git. Não envie dados pessoais, senhas, tokens ou arquivos `.env`/`secrets.toml` ao repositório. Configure segredos de desenvolvimento pelo gerenciador de secrets do Codespaces quando necessário.
