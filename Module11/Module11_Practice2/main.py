{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPcm1aXmZ7zolkM4XjMXAcN",
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
        "<a href=\"https://colab.research.google.com/github/AndrewLev34/COP1000-Python/blob/main/Module11/Module11_Practice2/main.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "f8VJcmOKlwns",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "37eab5b6-3b35-4752-a1a9-3a5438500e0f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "15\n",
            "5\n",
            "50\n",
            "2.0\n"
          ]
        }
      ],
      "source": [
        "import calculations\n",
        "\n",
        "print(calculations.add(10,5))\n",
        "\n",
        "print(calculations.subtract(10,5))\n",
        "\n",
        "print(calculations.multiply(10,5))\n",
        "\n",
        "print(calculations.divide(10,5))"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "userinput1 = int(input(\"Enter first number: \"))\n",
        "userinput2 = int(input(\"Enter second number: \"))\n",
        "\n",
        "print(calculations.add(userinput1,userinput2))\n",
        "\n",
        "print(calculations.subtract(userinput1,userinput2))\n",
        "\n",
        "print(calculations.multiply(userinput1,userinput2))\n",
        "\n",
        "if userinput2 == 0:\n",
        "    print(\"Cannot divide by zero\")\n",
        "else:\n",
        "    print(calculations.divide(userinput1,userinput2))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EWlCdGifyrXk",
        "outputId": "2c38c500-aef6-4711-fcbd-9c0a8c419540"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter first number: 19\n",
            "Enter second number: 7\n",
            "26\n",
            "12\n",
            "133\n",
            "2.7142857142857144\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import messages\n",
        "\n",
        "print(messages.title())\n",
        "print(messages.closing())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "X4tAJF4u0PYo",
        "outputId": "9839c03f-ffcb-4493-e9d2-d2d380e781cf"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Welcome to Python!\n",
            "Goodbye.\n"
          ]
        }
      ]
    }
  ]
}