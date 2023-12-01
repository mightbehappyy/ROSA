import discord


class ConfirmationEmbed:
    def send_confirmation_embed(self, motivation, start, end, date, name):
        embed = discord.Embed(
            title="Confirmação de reserva :white_check_mark:", color=0xFFFFFF
        )
        embed.add_field(name="Nome da reserva", value=f"```{motivation}```")
        embed.add_field(name="Nome do autor da reserva", value=f"```{name}```")
        embed.add_field(name="Data da reserva", value=f"```{date}```")
        embed.add_field(name="Horário do início", value=f"```{start}```")
        embed.add_field(name="Horário do termino", value=f"```{end}```")
        embed.add_field(name="", value="", inline=True)

        return embed
