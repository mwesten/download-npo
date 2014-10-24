**Download-gemist downloads videos from the Dutch npo.nl (formerly uitzending
gemist) site. The rest of the documentation is in Dutch.**


Download-gemist download videos van de [NPO][1] (voorheen ‘uitzending gemist’)
site van de publieke omroep. In principe zouden alle sites die gebruik maken van
de zogeten “NPOPlayer” moeten werken, zoals bv. ncrv.nl of nrc.nl (al zijn deze
niet allemaal getest).

Voor vragen of opmerkingen kun je mailen naar [martin@arp242.net][3].


Installatie
===========
- **[Windows installer][d-win]**
- **[Source][d-unix]**, voor BSD, Linux, UNIX, en OSX. [Python][2] is nodig
  (Python 2.6+ & 3.2+ zijn getest), voor de grafische interface is ook `Tkinter`
  nodig (deel van Python maar soms een aparte package).

Als je oudere Silverlight/Windows media player uitzendingen wilt downloaden heb
je [libmms][libmms] nodig. Dit werkt vooralsnog alleen op POSIX (ie.
niet-Windows) systemen. Dit is verder geheel optioneel.


Gebruik
=======
download-gemist is een commandline-tool, er is ook een grafische frontend
`download-gemist-gui`.

Voorbeeld:  
`download-gemist http://www.npo.nl/andere-tijden/23-10-2014/VPWON_1227038`

Overzicht van alle opties (dit is wat je te zien krijgt als je `download-gemist
-h` gebruikt):

	-h    Toon deze help
	-v    Toon versie
	-n    Download niks, laat zien wat we zouden doen
	-V    Print meer informatie naar het scherm. Gebruik -V twee keer voor nog meer info
	-s    Stil: geef geen informatieve berichten (alleen errors)
	-o    Zet output directory. Default is huidige directory
	-f    Zet output file, relatief aan -o. Default is titel van de video.
	      Gebruik - voor stdout
	-w    Overschrijf bestaande bestanden (default is om bestand over te slaan
	      als deze al bestaat)
	-c    Verwijder geen karakters in de bestandsnaam muv. spaties
	          - Als je -c 2x opgeeft, worden spaties ook behouden
	          - De default is om alle ongeldige FAT32/NTFS karakters te
	            verwijderen en spaties te vervangen door underscores
	-m    Toon enkel de metadata in YAML formaat
	-M    Toon enkel de metadata in JSON formaat
	-t    Download ook ondertiteling, als deze bestaat
	-T    Download alleen ondertiteling, geef een error als deze niet bestaan



FAQ
===

Help! Het werkt niet! PANIEK!
-----------------------------
Vaak is dit omdat er op de NPO site iets niet klopt; soms ontbreekt een
videobestand, of is het niet compleet. Meestal is dit een dag of wat later
opgelost.  
Werkt het een dag later nog niet, of denk je dat het niet de schuld van de site
is? Stuur dan even een email naar [martin@arp242.net][3] met de URL die je
gebruikt en de (volledige) output van je commando (het liefst met de `-VVV`
opties), dan zal ik er even naar kijken.

Kan ik ook een video streamen zonder het eerst op te slaan?
-----------------------------------------------------------
Uiteraard!

`download-gemist -f - http://www.npo.nl/andere-tijden/23-10-2014/VPWON_1227038 | mplayer -cache 4096 -cache-min 99 -`

Ondertitels worden opgeslagen als .srt, maar zijn eigenlijk in het WebVTT formaat?
----------------------------------------------------------------------------------
Dat klopt; WebVTT wordt vooralsnog door maar weinig spelers herkend, en het is
feitelijk hetzelfde als Subrip (`.srt`) ondertitels (de verschillen zijn miniem).


ChangeLog
=========

Versie 1.7, 2014-10-24
----------------------
- uitzendinggemist.nl is nu npo.nl, hernoem hier en daar dingen.
- Fix voor Python 2.6
- Fix voor lokale omroepen (omroep Brabant ed.)
- `-V` kan nu tot 3 keer opgegeven worden
- `-t` toevoegd om ook ondertitels mee te downloaden. Met `-T` worden alleen de
  ondertitels gedownload.
- `-m` om alleen de metadata te laten zien, in YAML formaat; `-M` voor JSON
  formaat.


Versie 1.6.3, 2014-02-18
------------------------
- Fixes in release, Windows-build van 1.6.2 was fubar


Versie 1.6.2, 2014-02-10
------------------------
- Fix voor huidige versie van de site
- Ondersteun ook oudere (MMS/ASF) uitzendingen


Versie 1.6.1, 2014-01-05
------------------------
- Bugfix: Uitzendingen die niet bij een serie horen gaven een error
- Iets betere errors in de GUI
- Aantal kleine verbeteringen


Versie 1.6, 2013-12-28
----------------------
- Geef waarschuwing als je een oudere versie gebruikt
- Werkt ook op andere sites met de NPOPlayer (npo.nl, ncrv.nl, etc.)
- Betere bestandsnamen
- Voeg grafische interface toe (`download-gemist-gui`)
- Windows installer
- `download-gemist-list` verwijderd; zo heel nuttig is het niet, en kost toch
  continue tijd om te onderhouden


Versie 1.5.1, 2013-10-09
------------------------
- Fix voor huidige versie van de site


Versie 1.5, 2013-10-06
----------------------
- `download-gemist-list` werkt nu ook bij `/weekarchief/` pagina’s
- Bugfix: Output bestand werd toch gemaakt bij `-n`
- Bugfix: `-p` bij `download-gemist-list` haalde altijd 1 pagina te veel op
- Bugfix: UnicodeError met python2 & `download-gemist-list`


Versie 1.4.2, 2013-10-01
------------------------
- Fix voor huidige versie van de site


Versie 1.4.1, 2013-09-23
------------------------
- Fix voor huidige versie van de site


Versie 1.4, 2013-08-22
----------------------
- Fix voor huidige versie van de site
- **Hernoem `download-gemist-guide` naar `download-gemist-list`**
- Gebruik nu overal Nederlands ipv. Engels of een mix van beide
- `download-gemist-list` leest nu ook van stdin
- `setup.py` script


Versie 1.3, 2013-03-05
----------------------
- Fix voor huidige versie van de site
- Betere voortgang-indicator


Versie 1.2, 2012-11-11
----------------------
- Voeg `download-gemist-guide` toe
- Voeg `-c` en `-w` opties toe
- Werkt nu ook met Python 3
- Fix voor huidige versie van de site


Versie 1.1, 2012-10-11
----------------------
- Geen `:` in bestandsnamen (problemen met FAT32)
- Fix voor huidige versie van de site


Versie 1.0, 2012-10-03
----------------------
- Eerste release



[1]: http://www.npo.nl/
[2]: http://python.org/
[3]: mailto:martin@arp242.net
[d-win]: https://bitbucket.org/Carpetsmoker/download-gemist/downloads/download-gemist-setup-1.7.exe
[d-unix]: https://bitbucket.org/Carpetsmoker/download-gemist/downloads/download-gemist-1.7.tar.gz
[libmms]: http://sourceforge.net/projects/libmms/