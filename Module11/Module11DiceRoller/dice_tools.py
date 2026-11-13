{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPxVlhrcot/Ala7O3ln5Uby",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/AndrewLev34/COP1000-Python/blob/main/Module11/Module11DiceRoller/dice_tools.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 15,
      "metadata": {
        "id": "Tpj00nwfFoVb"
      },
      "outputs": [],
      "source": [
        "import random\n",
        "\n",
        "def roll_die(sides):\n",
        "    return random.randint(1, sides)"
      ]
    }
  ]
}