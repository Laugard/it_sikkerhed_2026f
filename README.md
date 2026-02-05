# it_sikkerhed_2026f

Hej, mit navn er Lauge.
Dette er et skoleprojekt på Zealand Næstved (IT-sikkerhed) 1. Semester

Her er mine 4 nye unit tests:

<img width="589" height="431" alt="image" src="https://github.com/user-attachments/assets/97aadba2-cc19-4cf9-9986-e115be5b713a" />


Her er output:

<img width="791" height="837" alt="image" src="https://github.com/user-attachments/assets/857bac53-95a5-4d4c-932b-5f654590e837" />

----------

**Emne: Login-system med rate limiting (IT-sikkerhed)**

**Ækvivalensklasser**

Jeg har opdelt input til login i ækvivalensklasser for at sikre korrekt validering og robusthed. Gyldige klasser er f.eks. korrekt format på brugernavn og adgangskode samt gyldige længder. Ugyldige klasser omfatter tomme felter, for korte eller for lange adgangskoder samt ugyldigt format. Ved at teste én repræsentant fra hver klasse kan man dække mange tilfælde med få tests.

**Security gate**: Krav- og designfasen (valideringsregler defineres tidligt).

----------

**Grænseværditest**

Jeg tester grænseværdier for inputfelter som adgangskodelængde (fx minimum og maksimum tilladt længde). Det sikrer, at systemet håndterer værdier lige på grænsen korrekt og ikke tillader for korte eller for lange adgangskoder, som kan føre til svag sikkerhed eller fejl i systemet.

**Security gate**: Implementerings- og testfasen (inputvalidering verificeres).

-----------

**CRUD(L)**

Jeg tester oprettelse, læsning, opdatering og sletning af brugere (samt login-funktionen) for at sikre, at brugerkonti håndteres korrekt og sikkert. Fokus er på, at kun autoriserede brugere kan oprette og ændre data, og at sletning af brugere ikke efterlader følsomme data.

**Security gate**: Implementerings- og integrationsfasen (adgangskontrol og databeskyttelse).

--------

**Cycle process test**

Jeg tester hele login-processens livscyklus: registrering → login → fejl ved forkert login → låsning af konto efter for mange forsøg → oplåsning. Det sikrer, at sikkerhedsforanstaltninger som rate limiting og konto-låsning fungerer korrekt gennem hele flowet.

**Security gate**: Systemtest (end-to-end sikkerhedsflow).

-------

**Testpyramiden**

Jeg anvender testpyramiden ved primært at fokusere på unit tests af valideringslogik (fx password-regler), færre integrationstests af login-modulet mod databasen og få end-to-end tests af hele login-flowet. Det giver hurtig feedback og høj testdækning uden tunge tests overalt.

**Security gate**: Kontinuerlig test i CI/CD (automatiserede tests ved hver ændring).

-------

**Decision table test**

Jeg bruger decision tables til at teste kombinationer af betingelser i login-flowet, fx: korrekt/ukorrekt password, konto låst/ulåst, for mange loginforsøg ja/nej. Det sikrer, at alle kombinationer af regler og handlinger er dækket, så der ikke opstår sikkerhedshuller i edge cases.

**Security gate**: Design- og testfasen (regler for adgangskontrol valideres).
