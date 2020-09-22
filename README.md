# damasvue

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

npm install -g @vue/cli

npm install -g @vue/cli-service-global

### Jogo de damas em Vue
Regras do jogo:
- Peças andam somente nas diagonais, uma casa por vez.
- Uma peça come a adversária se a próxima casa na diagonal em sentido de avanço ao campo do adversário estiver vazia, passando por cima do adversário.
- Se uma peça chegar a ultima linha do campo de batalha inimigo, ela é promovida a dama podendo andar para frente ou traz, mantendo a regra de andar somente na diagonal uma casa por vez.
