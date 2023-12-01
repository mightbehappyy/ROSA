import discord


class HelpEmbed:
    @staticmethod
    def create_help_embed():
        embed = discord.Embed(
            title="Lista de Comandos :technologist: ",
            description="Aqui estão os comandos disponíveis:",
            color=0x7289DA,
        )

        commands = [
            (
                "/checar_reserva [lab]",
                "```Mostra as reservas para semana do laboratório escolhido (Windows ou Linux)```",
            ),
            (
                "/reservar [lab]",
                "```Serve para os professores reservarem suas aulas preenchendo um forms/modal```",
            ),
            (
                "/ppc",
                "```Envia o link do projeto pedagógico de curso de graduação de Engenharia de Software do Campus Garanhuns```",
            ),
            (
                "/graficotempo [cidade]",
                "```Retorna um gráfico com a progressão da temperatura, umidade e sensação térmica durante o dia```",
            ),
            ("/d20", "```Rola um dado de 20 lados```"),
            (
                "/tempo [cidade]",
                "```Retorna algumas informações do clima da cidade escolhida```",
            ),
            (
                "/deletar [numero de mensagens]",
                "```Para deletar mensagens quando o chat ficar muito poluído```",
            ),
            (
                "/oi",
                "```Eu me apresento 😎```",
            ),
        ]

        for command, description in commands:
            embed.add_field(name=command, value=description, inline=False)

        return embed
