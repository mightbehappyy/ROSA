<h1 align="center">
  <br>
  <a href="http://www.amitmerchant.com/electron-markdownify"><img src="https://i.imgur.com/Qn8f8o0.png" alt="ROSA" width="500"></a>
  <br>
  <br>
</h1>

<h1 align="center">ROSA BOT (Reserve Online Sua Aula) </h1>

> Reserve sua aula!

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)
[![wakatime](https://wakatime.com/badge/user/018bb0d6-56a3-43d5-85d1-e7b7401fdda3/project/018bbbaa-9b31-475a-ad1b-16c6c04441fe.svg)](https://wakatime.com/badge/user/018bb0d6-56a3-43d5-85d1-e7b7401fdda3/project/018bbbaa-9b31-475a-ad1b-16c6c04441fe)

ROSA é um bot para a plataforma Discord criada com o objetivo de facilitar a vida dos monitores dos laboratórios de computação do Campus UPE Garanhuns em suas reservas.
Apesar de seu propósito inicial, ROSA é um bot multiuso, e planejamos implementar funcionalidades interessantes no futuro como rolagem de dados para RPG e gerênciamento do servidor

## Comandos

| Comandos                         | Descrição                                                                                              |
| -------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `/checar_reserva [lab]`          | Mostra as reservas para semana do laboratório escolhido (Windows ou Linux)                             |
| `/reservar [lab]`                | Serve para os professores reservarem suas aulas preenchendo um forms/modal                             |
| `/ppc`                           | Envia o link do projeto pedagógico de curso de graduação de Engenharia de Software do Campus Garanhuns |
| `/tempo [cidade]`                | Retorna algumas informações do clima da cidade escolhida                                               |
| `/graficotempo  [cidade]`        | Retorna um gráfico com a progressão da temperatura, umidade e sensação termica durante o dia           |
| `/d20`                           | Rola um dado de 20 lados                                                                               |
| `/deletar [numero de mensagens]` | Para deletar mensagens quando o chat ficar muito poluído                                               |
| `/oi`                            | ROSA se apresenta 😎                                                                                   |

## Setup

```sh
pip install discord
```

Siga as intruções do guia de início rápido da API do [Google Calendar](https://developers.google.com/calendar/api/quickstart/python?hl=pt-br)

## Referências

[Python](https://docs.python.org/3.11/tutorial/index.html)  
[Discord.py](https://discordpy.readthedocs.io/en/stable/)  
[Discord](https://discord.com/developers/docs/intro)  
[Google Calendar](https://developers.google.com/calendar/api/quickstart/python?hl=pt-br)  
[WeatherAPI](https://www.weatherapi.com/docs/)  
[QuickChart](https://quickchart.io/documentation/)

## Histórico de Mudanças

- #### 0.1 ADD: Comando para checagem do horário semanal de reservas
- #### 0.2 ADD: Comando para reserva de Labs
- #### 0.3 ADD: Comando para checagem de horários semanais futuros (Em até 10 semanas)

## Autores

- [mightbehappyy](https://github.com/mightbehappyy)
