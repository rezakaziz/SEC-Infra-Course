# Sécurité des infrastructures logicielles et matérielles

Ce module présente les mécanismes essentiels de sécurisation des systèmes Linux et des applications Web. Les étudiants découvrent les principaux risques de sécurité, les mécanismes de protection des systèmes d'exploitation ainsi que les vulnérabilités applicatives les plus courantes et leurs contre-mesures.

Les travaux pratiques sont réalisés sur une machine virtuelle Debian utilisée tout au long du module.

## Objectifs pédagogiques

À l'issue du module, l'étudiant sera capable de :

- Identifier les principales menaces pesant sur un système Linux ;
- Mettre en œuvre des mécanismes d'authentification et de contrôle d'accès ;
- Appliquer les principes de défense en profondeur ;
- Sécuriser les principaux services d'un serveur Linux ;
- Identifier les vulnérabilités applicatives courantes ;
- Comprendre l'impact des vulnérabilités Web sur un système d'exploitation ;
- Proposer des mesures de protection adaptées à une plateforme logicielle.

## Planning des cours et TP

### Jour 1 — Sécurité des systèmes Linux

| Demi-journée | Cours (1h)                                                                            | TP (2h)                                                                                                                                 |
| ------------ | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Matin        | Principes fondamentaux de la sécurité et menaces sur les systèmes Linux               | Identification des données sensibles, analyse des permissions, protection des fichiers et répertoires sensibles                         |
| Après-midi   | Authentification, gestion des comptes, permissions Unix, ACL et défense en profondeur | Gestion des utilisateurs et groupes, configuration de PAM, utilisation de chmod, chown, getfacl et setfacl, sécurisation d'un accès SSH |

### Jour 2 — Sécurité des plateformes Web

| Demi-journée | Cours (1h)                                                                                                                                      | TP (2h)                                                                                                                        |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| Matin        | Vulnérabilités applicatives : injection SQL, inclusion de fichiers et injection de commandes                                                    | Exploitation contrôlée de vulnérabilités avec DVWA, analyse des impacts sur le système Linux                                   |
| Après-midi   | Sécurisation des plateformes Web : réduction de la surface d'attaque, protection des services Web et bonnes pratiques de développement sécurisé | Mise en œuvre de contre-mesures, sécurisation d'Apache, protection des ressources sensibles et analyse d'une configuration Web |

## Environnement de travaux pratiques

- Machine virtuelle Debian 12
- Apache
- PHP
- SSH
- PAM
- ACL
- DVWA

## Modalités d'évaluation

| Évaluation                        | Pondération |
| --------------------------------- | ----------- |
| Quiz de fin de journée            | 30 %        |
| Travaux pratiques et compte-rendu | 70 %        |

## Critères d'évaluation

- Compréhension des concepts de sécurité ;
- Maîtrise des mécanismes Linux étudiés ;
- Identification et analyse des vulnérabilités ;
- Pertinence des mesures de protection proposées ;
- Autonomie dans la réalisation des travaux pratiques.
