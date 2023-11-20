import discord
import traceback
from datetime import datetime
from CalendarAPI import post_event


class ReservationModal(discord.ui.Modal, title="Reserva"):
    motivation = discord.ui.TextInput(
        label="Nome da Cadeira, Monitoria ou Curso",
        placeholder="Ex: Programação 2",
        required=True,
    )

    name = discord.ui.TextInput(
        label="Nome do autor da reserva", placeholder="Ex: Pedro Luiz", required=True
    )

    date = discord.ui.TextInput(
        label="Data da reserva",
        placeholder="Ex: 18-11-2023",
        required=True,
        max_length=10,
        min_length=10,
    )

    start_time = discord.ui.TextInput(
        label="Horário do início",
        placeholder="Ex: 09:10 ",
        required=True,
        max_length=5,
        min_length=5,
    )

    ending_time = discord.ui.TextInput(
        label="Horário do termino",
        placeholder="Ex: 12:30 ",
        required=True,
        max_length=5,
        min_length=5,
    )

    async def on_submit(self, interaction: discord.Interaction):
        motivation_value = self.motivation.value
        name_value = self.name.value
        date_value = self.date.value
        start_time_value = self.start_time.value
        ending_time_value = self.ending_time.value

        try:
            date_obj = datetime.strptime(date_value, "%d-%m-%Y")
            formatted_date = date_obj.strftime("%Y-%m-%d")
        except ValueError as e:
            await interaction.response.send_message(
                "Formato de data inválido por favor use: Dia-Mês-Ano.", ephemeral=True
            )
            print(e)

        try:
            datetime.strptime(start_time_value, "%H:%M")
            datetime.strptime(ending_time_value, "%H:%M")
        except ValueError as e:
            await interaction.response.send_message(
                "Formato de hora inválido por favor use: Hora:Minuto.", ephemeral=True
            )
            print(e)
            return

        try:
            event = post_event(
                motivation_value, start_time_value, ending_time_value, formatted_date
            )
            print(event)
            if event == True:
                await interaction.response.send_message(
                    "Já existe uma reserva para esse horário :cry:", ephemeral=True
                )
                return
            else:
                user = await interaction.client.fetch_user(interaction.user.id)
            await user.send(
                f"Reserva enviada com sucesso :white_check_mark:\n\nMotivação: {motivation_value}\nNome: {name_value}\nData: {date_value}\nHorário: {start_time_value} - {ending_time_value}"
            )

        except Exception as e:
            await interaction.response.send_message(
                "Ocorreu um erro ao enviar a reserva :cry:",
                ephemeral=True,
            )

    async def on_error(
        self, interaction: discord.Interaction, error: Exception
    ) -> None:
        await interaction.response.send_message(
            "Oops! Something went wrong.", ephemeral=True
        )

        # Make sure we know what the error actually is
        traceback.print_exception(type(error), error, error.__traceback__)
