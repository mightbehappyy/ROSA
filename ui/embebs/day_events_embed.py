import discord

from apis.services.calendar_service import CalendarService
from utils.functions.translate_day import translate



class DayEventsEmbed:
    def __init__(self, lab):
        self.calendar_service = CalendarService(lab)
        self.lab = lab

    def get_week_events_embed(self, date):
        events_by_day = self.calendar_service.get_todays_events(date)

        embed = discord.Embed(
            title="Infelizmente não foi possível reservar nesse horário :cry:",
            description=f"Aqui está os horários disponíveis, tente reservar sua aula para outro horário se possível",
            color=0xF03A17,
        )

        for day, events in events_by_day.items():
            day_events = "\n".join(
                f"Reserva para: {event['summary']} \nHorário: {event['start']} às {event['end']}\n"
                for event in events
            )

            embed.add_field(
                name=f"{translate(day)}",
                value=f"```{day_events}```",
                inline=False,
            )

        if not events_by_day:
            embed.add_field(
                name="Nenhum evento encontrado",
                value="Não há horários reservados para essa semana",
                inline=False,
            )

        return embed
