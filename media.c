#include <stdio.h>

float menor_nota(float notas[]) {
    float menor = notas[0];
    int i = 0;

    while (i < 5) {
        if (notas[i] < menor) {
            menor = notas[i];
        }

        i++;
    }

    return menor;
}

float calcula_media(float notas[], float menor) {
    float soma = .0;

    for (int i = 0; i < 5; i++) {
        soma += notas[i];
    }

    float media = (soma - menor) / 4;

    return media;
}

int main() {
    float P[5];

    for (int i = 0; i < 5; i++) {
        scanf("%f", &P[i]);
    }

    float media = calcula_media(P, menor_nota(P));

    printf("\n%.2f\n", media);

    return 0;
}
