# Calculadora Lib (ps_calculadora_lib)

Uma biblioteca leve e flexível para operações aritméticas e avaliação de expressões — ideal para projetos Node.js, front-ends e scripts que precisam de cálculos confiáveis e fáceis de usar.

> Observação: este README é um modelo completo e opinativo. Ajuste nomes de pacotes, assinaturas de funções e exemplos conforme a API real do seu repositório.

## Índice

- Sobre
- Principais funcionalidades
- Instalação
- Uso rápido
- API (exemplos)
- Configuração e opções avançadas
- Tratamento de erros e precisão
- Test
- Contribuindo
- Roadmap
- Licença
- Contato

## Sobre

O objetivo da calculadora-lib é fornecer um conjunto claro e testado de operações matemáticas (soma, subtração, multiplicação, divisão, potenciação, radiciação) e uma função de avaliação de expressões que seja segura e previsível. A biblioteca prioriza:

- Simplicidade de uso
- Resultados consistentes (com controle de precisão)
- Baixa dependência e footprint pequeno
- API adequada para uso em Node.js e navegadores (via bundlers ou builds UMD/ESM)

## Principais funcionalidades

- Operações básicas: add, sub, mul, div
- Operações avançadas: pow, sqrt, abs, percent
- Avaliação de expressões matemáticas com segurança básica (evita execução de código arbitrário)
- Controle de precisão (número de casas decimais)
- Export compatível com CommonJS e ES Modules
- Pequena e sem dependências externas (configurável)

## Instalação

Via npm:
```bash
npm install ps_calculadora_lib
```

Via yarn:
```bash
yarn add ps_calculadora_lib
```

Uso via CDN (ex.: distribuído em /dist/ps_calculadora_lib.umd.js)
```html
<script src="https://cdn.exemplo.com/ps_calculadora_lib/ps_calculadora_lib.umd.min.js"></script>
<script>
  // Exemplo: window.PSCalculadoraLib
</script>
```

> Substitua as URLs de CDN e o nome do pacote conforme publicado no registry.

## Uso rápido

Importando como ES Module:
```javascript
import { add, sub, mul, div, evaluate } from 'ps_calculadora_lib';

console.log(add(2, 3));        // 5
console.log(sub(10, 4));       // 6
console.log(mul(3, 5));        // 15
console.log(div(10, 2));       // 5

console.log(evaluate('2 + 3 * (7 - 4)')); // 11
```

Importando como CommonJS:
```javascript
const { add, evaluate } = require('ps_calculadora_lib');

console.log(add(1.5, 2.25)); // 3.75
console.log(evaluate('10 / 4 + 0.5')); // 3
```

## API (exemplos de função)

Abaixo está uma API sugerida. Ajuste conforme a implementação real da sua biblioteca.

- add(a: number, b: number): number
  - Soma dois números.
  - Ex.: add(2, 3) => 5

- sub(a: number, b: number): number
  - Subtrai b de a.
  - Ex.: sub(5, 2) => 3

- mul(a: number, b: number): number
  - Multiplica dois números.
  - Ex.: mul(4, 2.5) => 10

- div(a: number, b: number): number | throws
  - Divide a por b. Deve lançar erro ao dividir por zero.
  - Ex.: div(10, 2) => 5

- pow(base: number, exponent: number): number
  - Potenciação.
  - Ex.: pow(2, 3) => 8

- sqrt(value: number): number
  - Raiz quadrada (lança em números negativos, a menos que haja suporte para complexos).
  - Ex.: sqrt(9) => 3

- percent(value: number, of?: number): number
  - Calcula porcentagem (ex.: percent(10, 200) => 20). Se `of` omitido, retorna value / 100.

- evaluate(expression: string, options?: EvaluateOptions): number
  - Avalia uma expressão aritmética segura (somente operadores matemáticos e parênteses).
  - Ex.: evaluate('3 + 4 * (2 - 1)') => 7
  - options sugeridas:
    - precision?: number (número de casas decimais)
    - safe?: boolean (forçar parsing seguro; padrão true)

Exemplo com configuração de precisão:
```javascript
import { evaluate, setPrecision } from 'ps_calculadora_lib';

setPrecision(4);
console.log(evaluate('10 / 3')); // 3.3333
```

## Configuração e opções avançadas

- Controle de precisão: fornecer função global ou parâmetro opcional por chamada.
- Localização: retorno de strings formatadas (ex.: toLocaleString) não é responsabilidade do core — deixe para a camada de apresentação.
- Plugins/Extensões: considere suportar registros de funções personalizadas (ex.: registerFunction('sin', fn)) se desejar expandir para funções trigonométricas.

## Tratamento de erros e segurança

- Nunca execute expressão JS diretamente via eval. Use um parser matemático (ou um parser próprio) que valide tokens permitidos: números, operadores (+ - * / ^ %), parênteses, funções pré-registradas.
- Em divisões, lance erro para divisão por zero:
  - throw new Error('Divisão por zero') ou retorne NaN dependendo do design (documente a escolha).
- Valide entradas: lance TypeError para argumentos não numéricos quando apropriado.

## Test

Sugestão de configuração (jest):
```bash
npm install --save-dev jest
```

Exemplo de script package.json:
```json
{
  "scripts": {
    "test": "jest --coverage",
    "build": "rollup -c",
    "lint": "eslint src/**"
  }
}
```

Exemplo de teste simples (Jest):
```javascript
const { add, div, evaluate } = require('../dist'); // ajuste o caminho conforme necessário

test('soma simples', () => {
  expect(add(2, 2)).toBe(4);
});

test('divisão por zero lança erro', () => {
  expect(() => div(1, 0)).toThrow(/Divisão por zero/);
});

test('avalia expressão composta', () => {
  expect(evaluate('2 + 3 * 4')).toBe(14);
});
```

## Contribuindo

Contribuições são bem-vindas! Sugestões:

1. Abra uma issue descrevendo o problema ou feature.
2. Crie um branch a partir de main com um nome claro: `feature/nome-da-feature` ou `fix/descricao`.
3. Faça commits pequenos e bem descritos.
4. Abra um Pull Request com descrição dos testes e comportamento esperado.

Guia rápido:
- Siga o estilo do código do projeto (ESLint / Prettier).
- Inclua testes para novas funcionalidades e correções.
- Atualize README e changelog conforme necessário.

## Roadmap (sugestões)

- Suporte a funções trigonométricas (sin, cos, tan)
- Modo com BigNumber para alta precisão (para finanças)
- Build para browsers (UMD) e suporte a CDN pública
- Internacionalização de mensagens de erro

## Licença

Escolha uma licença adequada (ex.: MIT). Exemplo:

MIT © 2025 Lucas Mariani G

Inclua o arquivo LICENSE no repositório.

## Contato

Desenvolvedor: Lucas Mariani G  
GitHub: https://github.com/LucasMarianiG

Se quiser, eu posso:
- Ajustar o README para refletir a API real do seu código (me envie os nomes de funções/exports).
- Criar um arquivo README.md já com badges (build, coverage, npm) e com links reais (CI, npm).
- Gerar exemplos de testes e um template de GitHub Actions para CI.
