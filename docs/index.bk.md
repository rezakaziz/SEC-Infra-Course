# 🔐 Sécurité des infrastructures logicielles et matérielles

Ce module présente les mécanismes fondamentaux de sécurité des systèmes d’exploitation Linux et des plateformes logicielles. Il aborde la protection des données, les vulnérabilités des systèmes, les attaques informatiques, l’authentification, le contrôle d’accès et le confinement des applications, ainsi que les vulnérabilités applicatives pouvant affecter la sécurité d’une infrastructure informatique.

Les travaux pratiques sont réalisés sur une machine virtuelle Linux utilisée tout au long du module afin de mettre progressivement en œuvre les mécanismes étudiés.

---

## 🎯 Objectifs pédagogiques

À l’issue de ce module, l’étudiant sera capable de :

- Identifier les données sensibles d'un système d'exploitation ;
- Comprendre les principales vulnérabilités des systèmes Linux ;
- Reconnaître les principales catégories d'attaques informatiques ;
- Analyser un incident de sécurité sur un système Linux ;
- Mettre en œuvre des politiques d'authentification sous Linux ;
- Configurer des mécanismes de contrôle d'accès ;
- Comprendre les principes du confinement d'applications ;
- Identifier les impacts des vulnérabilités applicatives sur un système Linux ;
- Participer à la sécurisation d'une plateforme logicielle hébergée sous Linux.

---

## 📅 Planning des cours et TP

| Séance | Cours                                                                                                                                                                                                                                              | TP                                                                                                                                                                                                      |
| :----: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **01** | **Protection des données et sécurité de l'information dans les systèmes d'exploitation** : confidentialité, intégrité, disponibilité, données sensibles, menaces sur les données et mécanismes de protection fournis par le système d'exploitation | **Protection des données dans un système Linux** : identification des données sensibles, analyse des permissions, vérification de l'intégrité des fichiers et mise en œuvre de mécanismes de sauvegarde |
| **02** | **Vulnérabilités des systèmes d’exploitation** : notion de vulnérabilité, erreurs de configuration, divulgation d'informations, traversée de répertoires, élévation de privilèges et gestion des vulnérabilités                                    | **Analyse d'une vulnérabilité système** : exploitation contrôlée d'une vulnérabilité de divulgation de fichiers, identification des causes et proposition de mesures correctives                        |
| **03** | **Typologie des attaques informatiques et analyse d'incidents** : logiciels malveillants, exploitation de vulnérabilités, compromission de comptes, élévation de privilèges, détection et analyse d'incidents de sécurité                          | **Analyse d'un incident de sécurité** : identification de fichiers suspects, analyse des processus, des journaux système et des connexions réseau                                                       |
| **04** | **Authentification sous Linux et PAM** : identification, authentification, autorisation, gestion des comptes, politiques de mots de passe, verrouillage et expiration des comptes                                                                  | **Renforcement des politiques d'authentification** : configuration de PAM, complexité des mots de passe, limitation des tentatives de connexion et expiration des mots de passe                         |
| **05** | **Contrôle d'accès et confinement sous Linux** : utilisateurs, groupes, permissions Unix, ACL, principe du moindre privilège, limites du DAC, principe du MAC, introduction à AppArmor et confinement des applications                             | **Gestion des permissions et confinement d'applications** : utilisation de chmod, chown, getfacl, setfacl, découverte des profils AppArmor et analyse d'un cas de confinement                           |
| **06** | **Vulnérabilités des plateformes logicielles** : surface d'attaque des applications Web, injection SQL, inclusion de fichiers, injection de commandes, impacts sur le système d'exploitation et mesures de protection                              | **Analyse de vulnérabilités applicatives avec DVWA** : exploitation contrôlée de SQL Injection, File Inclusion et Command Injection, analyse des impacts et identification des contre-mesures           |

---

## 🖥️ Environnement de travaux pratiques

### Machine virtuelle

```text
Debian 12
Apache
PHP
SSH
ACL
AppArmor
DVWA
```

Cette machine virtuelle est utilisée durant l'ensemble du module afin de mettre progressivement en œuvre les différents mécanismes de sécurité étudiés.

Les travaux pratiques couvrent notamment :

- la protection des données ;
- l'analyse de vulnérabilités système ;
- l'analyse d'incidents de sécurité ;
- l'authentification avec PAM ;
- le contrôle d'accès avec les permissions Unix et les ACL ;
- le confinement d'applications avec AppArmor ;
- l'analyse de vulnérabilités applicatives avec DVWA.

AppArmor est utilisé pour illustrer les mécanismes de contrôle d'accès obligatoire et le confinement des applications sous Linux.

---

## 📝 Modalités d'évaluation

L'évaluation du module repose exclusivement sur le contrôle continu.

| Évaluation                            | Pondération |
| ------------------------------------- | ----------: |
| Quiz de séance (6 quiz de 15 minutes) |        40 % |
| Travaux pratiques (comptes rendus)    |        60 % |

### Quiz de séance

À chaque séance, un quiz de 15 minutes permet de vérifier l'acquisition des notions abordées dans le cours précédent.

Les questions sont sous format de QCM.

### Travaux pratiques

Les travaux pratiques permettent d'évaluer la capacité de l'étudiant à :

- mettre en œuvre les mécanismes de sécurité étudiés ;
- analyser une configuration système ;
- identifier des vulnérabilités ;
- analyser un incident de sécurité ;
- appliquer des mesures de protection ;
- justifier les choix réalisés lors de la sécurisation d'un système Linux.

### Critères d'évaluation

Les évaluations prennent en compte :

- la compréhension des concepts de sécurité ;
- la maîtrise des outils et mécanismes Linux étudiés ;
- la qualité de l'analyse ;
- la pertinence des solutions proposées ;
- l'autonomie dans la réalisation des travaux pratiques.
