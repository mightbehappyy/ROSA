import discord

from src.apis.services.calendar_service import CalendarService
from src.utils.functions.translate_day import translate_day


class WeekEventsEmbed:
    def __init__(self, lab):
        self.calendar_service = CalendarService(lab)
        self.lab = lab

    def get_week_events_embed(self):
        date_range = self.calendar_service.get_calendar_week_range()
        events_by_day = self.calendar_service.get_calendar_events()

        embed = discord.Embed(
            title="Reservas do Laboratório Windows",
            description=f"Horário da semana para as reservas dos laboratórios \n `{date_range}`",
            color=0xF03A17,
        )

        for day, events in events_by_day.items():
            day_events = "\n".join(
                f"Reserva para: {event['summary']} \nHorário: {event['start']} às {event['end']}\n"
                for event in events
            )

            embed.add_field(
                name=f"{translate_day(day)}",
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
