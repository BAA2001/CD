1. SSH-sleutel en machtigingen:

    Probleem: Ik stuitte op problemen met betrekking tot de machtigingen van mijn SSH-sleutel, zowel in de workflow als op mijn VPS.
    Oplossing: Zorg ervoor dat de SSH-privésleutel de juiste machtigingen heeft en correct is geconfigureerd op de VPS. De SSH-sleutel mag geen wachtwoord hebben en moet veilig worden opgeslagen als een GitHub-geheim.

2. Klonen van het repository:

    Probleem: Toen ik het repository op mijn VPS wilde klonen, had ik problemen met het repository-pad.
    Oplossing: Verifieer of de Git-repository-URL en het pad correct zijn in de implementatiestap. Zorg ervoor dat de VPS-gebruiker de vereiste machtigingen heeft om toegang te krijgen tot het repository.

3. Servicenaam en servicemanager:

    <!-- Probleem: Ik moest mijn Flask-toepassingsservice herstarten, maar wist niet welke servicenaam of servicemanager ik moest gebruiken. -->
    Oplossing: Identificeer de servicenaam en servicemanager door actieve services op de VPS te vermelden met systemctl list-units --type=service. Gebruik de juiste servicenaam bij het herstarten van de service.

