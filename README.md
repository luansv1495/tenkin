[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Tenkin

Tenkin é um framework [WSGI] para aplicações web.

## Instalando

O Projeto ainda esta em desenvolvimento, portanto, ainda não foi criado um pacote python para instalação remoto via [pip], mas para testes e desenvolvimento do sistema voçê pode
usar a instalação local de pacotes do pip.

1. Puxe o repositório para seu computador.

```sh
git clone https://github.com/luansv1495/tenkin.git
```

2. Acesse a pasta do repositório.

```sh
cd tenkin
```

3. Utilize este comando para fazer a instalação em sua máquina.

```sh
pip install .
```

4. Verifique a instalação

```sh
python -m tenkin
```

## Exemplo

1. Use o comando 'create' para criar a estrutura básica de um projeto tenkin. Sera solicitado um nome para o projeto.

```sh
python -m tenkin create
```

2. Use o comando 'run' para executar o projeto em um ambiente de desenvolvimento.

```sh
python -m tenkin run
```

3. Acesse a partir de qualquer navegador com a url 'http://localhost:8000'

[WSGI]: https://wsgi.readthedocs.io
[pip]: https://pip.pypa.io/en/stable/quickstart/

[forks-shield]: https://img.shields.io/github/forks/luansv1495/tenkin?style=for-the-badge
[forks-url]: https://github.com/luansv1495/tenkin/network/members
[stars-shield]: https://img.shields.io/github/stars/luansv1495/tenkin?style=for-the-badge
[stars-url]: https://github.com/luansv1495/tenkin/stargazers
[issues-shield]: https://img.shields.io/github/issues/luansv1495/tenkin?style=for-the-badge
[issues-url]: https://github.com/luansv1495/tenkin/issues
