{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "1_Aula de DataScience",
      "provenance": [],
      "authorship_tag": "ABX9TyP0U3JrNssMhtWU0i7nAmQZ",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
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
        "<a href=\"https://colab.research.google.com/github/Mendes1302/Python-Learning/blob/master/IA/ANALYZE%20CINEMA%20DATA.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "P0uiPcPuPR59",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 212
        },
        "outputId": "8c8f7d74-3133-4686-dab6-b265f607a925"
      },
      "source": [
        "import pandas as pd\n",
        "\n",
        "url = \"https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula4.1/movies.csv\"\n",
        "dataFrame = pd.read_csv(url)\n",
        "dataFrame.columns = [\"Filmes_ID\", \"Título\", \"Gênero\"]\n",
        "dataFrame.head()\n",
        "\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Filmes_ID</th>\n",
              "      <th>Título</th>\n",
              "      <th>Gênero</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>Toy Story (1995)</td>\n",
              "      <td>Adventure|Animation|Children|Comedy|Fantasy</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>Jumanji (1995)</td>\n",
              "      <td>Adventure|Children|Fantasy</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>Grumpier Old Men (1995)</td>\n",
              "      <td>Comedy|Romance</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>Waiting to Exhale (1995)</td>\n",
              "      <td>Comedy|Drama|Romance</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>Father of the Bride Part II (1995)</td>\n",
              "      <td>Comedy</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   Filmes_ID  ...                                       Gênero\n",
              "0          1  ...  Adventure|Animation|Children|Comedy|Fantasy\n",
              "1          2  ...                   Adventure|Children|Fantasy\n",
              "2          3  ...                               Comedy|Romance\n",
              "3          4  ...                         Comedy|Drama|Romance\n",
              "4          5  ...                                       Comedy\n",
              "\n",
              "[5 rows x 3 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "abAWpdnOV642",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 195
        },
        "outputId": "8fd9f7d0-c580-4034-cfe3-740af2943e70"
      },
      "source": [
        "uri = \"https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula1.2/ratings.csv\"\n",
        "notas = pd.read_csv(uri)\n",
        "notas.columns = [\"Usuario_Id\", \"Filmes_ID\", \"Notas\", \"Momento\"]\n",
        "notas.head()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Usuario_Id</th>\n",
              "      <th>Filmes_ID</th>\n",
              "      <th>Notas</th>\n",
              "      <th>Momento</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>4.0</td>\n",
              "      <td>964982703</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>4.0</td>\n",
              "      <td>964981247</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1</td>\n",
              "      <td>6</td>\n",
              "      <td>4.0</td>\n",
              "      <td>964982224</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1</td>\n",
              "      <td>47</td>\n",
              "      <td>5.0</td>\n",
              "      <td>964983815</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1</td>\n",
              "      <td>50</td>\n",
              "      <td>5.0</td>\n",
              "      <td>964982931</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   Usuario_Id  Filmes_ID  Notas    Momento\n",
              "0           1          1    4.0  964982703\n",
              "1           1          3    4.0  964981247\n",
              "2           1          6    4.0  964982224\n",
              "3           1         47    5.0  964983815\n",
              "4           1         50    5.0  964982931"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nJKYlJbOX0qB",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "0bd27db6-6677-4edb-fd29-d8da29558891"
      },
      "source": [
        "notas [\"Notas\"].head()# 5 primeiros\n",
        "notas[\"Notas\"].unique()#Quais são os valores"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([4. , 5. , 3. , 2. , 1. , 4.5, 3.5, 2.5, 0.5, 1.5])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "J9KQeBHDYYhZ",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "cb5f414b-5000-4f40-820b-f30a833797e4"
      },
      "source": [
        "notas[\"Notas\"].mean()#Media\n",
        "notas[\"Notas\"].min()#Minimo"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0.5"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 18
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vrhAP-y5Y5wa",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 284
        },
        "outputId": "24669932-ddfd-4325-8a6b-a4ea790253cf"
      },
      "source": [
        "notas.describe()#Estatistica"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Usuario_Id</th>\n",
              "      <th>Filmes_ID</th>\n",
              "      <th>Notas</th>\n",
              "      <th>Momento</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>100836.000000</td>\n",
              "      <td>100836.000000</td>\n",
              "      <td>100836.000000</td>\n",
              "      <td>1.008360e+05</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>326.127564</td>\n",
              "      <td>19435.295718</td>\n",
              "      <td>3.501557</td>\n",
              "      <td>1.205946e+09</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>182.618491</td>\n",
              "      <td>35530.987199</td>\n",
              "      <td>1.042529</td>\n",
              "      <td>2.162610e+08</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.500000</td>\n",
              "      <td>8.281246e+08</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>177.000000</td>\n",
              "      <td>1199.000000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>1.019124e+09</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>325.000000</td>\n",
              "      <td>2991.000000</td>\n",
              "      <td>3.500000</td>\n",
              "      <td>1.186087e+09</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>477.000000</td>\n",
              "      <td>8122.000000</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>1.435994e+09</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>610.000000</td>\n",
              "      <td>193609.000000</td>\n",
              "      <td>5.000000</td>\n",
              "      <td>1.537799e+09</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "          Usuario_Id      Filmes_ID          Notas       Momento\n",
              "count  100836.000000  100836.000000  100836.000000  1.008360e+05\n",
              "mean      326.127564   19435.295718       3.501557  1.205946e+09\n",
              "std       182.618491   35530.987199       1.042529  2.162610e+08\n",
              "min         1.000000       1.000000       0.500000  8.281246e+08\n",
              "25%       177.000000    1199.000000       3.000000  1.019124e+09\n",
              "50%       325.000000    2991.000000       3.500000  1.186087e+09\n",
              "75%       477.000000    8122.000000       4.000000  1.435994e+09\n",
              "max       610.000000  193609.000000       5.000000  1.537799e+09"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 19
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "0W55N0D6Zfn1",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 282
        },
        "outputId": "57a35ca1-0021-4b77-e441-8d04d3e616f1"
      },
      "source": [
        "notas['Notas'].hist()\n",
        "\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f6a3d78df60>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 42
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "mE-ldOmTwaZ1"
      },
      "source": [
        "  "
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}