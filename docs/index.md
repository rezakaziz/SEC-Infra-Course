# Sécurité des infrastructures logicielles et matérielles

Ce module introduit les principes fondamentaux de la sécurité des systèmes d'information à travers l'étude des systèmes Linux et des applications Web. Les étudiants découvrent les objectifs de sécurité (confidentialité, intégrité et disponibilité), les principales ressources sensibles d'un système Linux ainsi que les mécanismes de protection permettant de limiter les risques de compromission.

Le module aborde les mécanismes d'authentification, d'autorisation et de contrôle d'accès, les permissions Unix, les ACL, la gestion des comptes et les principes de défense en profondeur. Les étudiants apprennent également à identifier les vulnérabilités applicatives les plus courantes, aussi bien côté client que côté serveur, et à comprendre leurs impacts sur les systèmes d'exploitation et les données.

Les travaux pratiques sont réalisés sur une machine virtuelle Debian utilisée tout au long du module afin de mettre en œuvre les mécanismes étudiés et d'analyser des scénarios réalistes d'attaque et de défense.

## Objectifs pédagogiques

À l'issue du module, l'étudiant sera capable de :

- Expliquer les principes fondamentaux de la sécurité de l'information ;
- Identifier les ressources et données sensibles d'un système Linux ;
- Analyser les principales menaces visant les systèmes Linux et les applications Web ;
- Mettre en œuvre des mécanismes d'authentification, d'autorisation et de contrôle d'accès ;
- Utiliser les permissions Unix et les ACL pour protéger les ressources système ;
- Appliquer les principes de défense en profondeur et du moindre privilège ;
- Identifier et analyser les principales vulnérabilités applicatives côté client et côté serveur ;
- Comprendre les impacts des vulnérabilités Web sur la sécurité d'une plateforme logicielle ;
- Proposer et mettre en œuvre des mesures de protection adaptées à une infrastructure logicielle.

## Planning des cours et TP

### Jour 1 — Sécurité des systèmes Linux

| Demi-journée | Cours (1h)                                                                                                                    | TP (2h)                                                                                                                                  |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Matin        | Fondements de la sécurité : confidentialité, intégrité, disponibilité, ressources sensibles et menaces sur les systèmes Linux | Identification des données sensibles, exploration de l'arborescence Linux, analyse des permissions et protection des fichiers sensibles  |
| Après-midi   | Authentification, autorisation, gestion des comptes, permissions Unix, ACL et défense en profondeur                           | Gestion des utilisateurs et groupes, utilisation de chmod, chown, getfacl et setfacl, configuration de PAM et sécurisation des accès SSH |

### Jour 2 — Sécurité des applications Web

| Demi-journée | Cours (1h)                                                                                                                                | TP (2h)                                                                                                                         |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Matin        | Sécurité Web côté client : navigateur, sessions, cookies, XSS, CSRF, vol de session et Clickjacking                                       | Analyse de scénarios d'attaque Web et observation des mécanismes de protection dans le navigateur                               |
| Après-midi   | Sécurité Web côté serveur : injection SQL, inclusion de fichiers, injection de commandes, logique métier et sécurisation des applications | Exploitation contrôlée de vulnérabilités avec DVWA, analyse des impacts sur le système Linux et mise en œuvre de contre-mesures |

## Environnement de travaux pratiques

- Machine virtuelle Debian 12
- Apache
- PHP
- SSH
- PAM
- ACL
- DVWA

## Modalités d'évaluation

| Évaluation                           | Pondération |
| ------------------------------------ | ----------- |
| Quiz de validation des connaissances | 50 %        |
| Travaux pratiques et compte-rendu    | 50 %        |

## Critères d'évaluation

- Compréhension des concepts fondamentaux de sécurité ;
- Maîtrise des mécanismes de protection Linux étudiés ;
- Capacité à identifier et analyser des vulnérabilités ;
- Pertinence des mesures de protection proposées ;
- Qualité de l'analyse de sécurité réalisée ;
- Autonomie dans la réalisation des travaux pratiques.
