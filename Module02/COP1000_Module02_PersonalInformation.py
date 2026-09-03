{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPdoz3A7CH9XHiP+RxxzbhP",
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
        "<a href=\"https://colab.research.google.com/github/AndrewLev34/COP1000-Python/blob/main/Module02/COP1000_Module02_PersonalInformation.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 12,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dc92Vw_zB2oG",
        "outputId": "fff53ddb-81e0-48bf-e61a-c703a1d40d1a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter first name here:Andrew\n",
            "Enter last name here:Leverette\n",
            "Enter age here:19\n",
            "Enter city here:Fleming Island\n",
            "Enter academic interest here:Data Science\n",
            "\n",
            "---Personal Information---\n",
            "\n",
            "first name: Andrew\n",
            "last name: Leverette\n",
            "age: 19\n",
            "age next year: 20\n",
            "city: Fleming Island\n",
            "academic interest: Data Science\n"
          ]
        }
      ],
      "source": [
        "\"\"\"Ask User for:\n",
        "first name\n",
        "last name\n",
        "age\n",
        "city\n",
        "academic interest\"\"\"\n",
        "\n",
        "f_name = input(\"Enter first name here:\")\n",
        "l_name = input(\"Enter last name here:\")\n",
        "age = int(input(\"Enter age here:\"))\n",
        "city = input(\"Enter city here:\")\n",
        "interest = input(\"Enter academic interest here:\")\n",
        "print()\n",
        "print(\"---Personal Information---\")\n",
        "print()\n",
        "print(f\"first name: {f_name}\")\n",
        "print(f\"last name: {l_name}\")\n",
        "print(f\"age: {age}\")\n",
        "print(f\"age next year: {age + 1}\")\n",
        "print(f\"city: {city}\")\n",
        "print(f\"academic interest: {interest}\")"
      ]
    }
  ]
}