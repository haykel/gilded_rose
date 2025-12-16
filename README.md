# Gilded Rose Kata – Python

## 📌 Description

Ce projet est une implémentation du **kata Gilded Rose** en Python.

---

## 📜 Règles de gestion

* Chaque produit a :

  * `sell_in` : nombre de jours restants pour vendre l’article
  * `quality` : valeur de qualité de l’article
* À la fin de chaque journée :

  * `sell_in` diminue de 1
  * `quality` évolue selon le type de produit

### Règles spécifiques

* La qualité ne peut jamais être négative
* La qualité ne dépasse jamais 50
* **Aged Brie** :

  * la qualité augmente avec le temps
  * augmente deux fois plus vite après expiration
* **Backstage passes** :

  * +1 quand `sell_in > 10`
  * +2 quand `sell_in ≤ 10`
  * +3 quand `sell_in ≤ 5`
  * qualité tombe à 0 après le concert
* **Sulfuras** :

  * produit légendaire
  * `sell_in` et `quality` ne changent jamais (`quality = 80`)
* **Conjured** :

  * la qualité se dégrade deux fois plus vite
  * quatre fois plus vite après expiration

⚠️ La classe `Item` ne doit jamais être modifiée.

---

## ▶️ Exécuter le programme

Le fichier `main.py` permet de visualiser l’évolution des produits **jour par jour**.

### Lancer le programme

```bash
python main.py
```

À chaque jour, appuie sur **Entrée** pour passer au jour suivant.

---

## 🧪 Lancer les tests

Les tests sont écrits avec **pytest** et couvrent les règles principales du kata.

### Installer pytest

```bash
pip install pytest
```

### Lancer les tests

```bash
pytest
```

Si tout est correct, tu verras :

```text
test_gilded_rose.py ...... [100%]
```

---


## 👤 JABRI HAYKEL 
