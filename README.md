# Autômatos e Máquina de Mealy
 
Trabalho desenvolvido na disciplina Teoria da Computação do Programa de Pós-Graduação em Ciência da Computação (PPGCC). Trabalho desenvolvido pelo aluno de doutorado Rafael Rocha. O trabalho consiste em densenvolver autômato finito e máquina de Mealy para determinadas tarefas.

## Autômato

Implementar um autômato finito deterministico (AFD) que aceitem as seguintes cadeias:

* Todas as cadeias em {0,1}* que apresentam cada 1 seguido imediatamente de dois 0.
* Todoas as cadeias em {a,b}* de modo que o último símbolo seja b e o número de símbolos a seja par.

## Autômato para busca de padrão

Implementar um autômato finito que reconheça todas as ocorrências da palavra computador no texto T. O programa deve apontar em quais posições ocorreram o casamento exato da palavra.

T = “O computador é uma máquina capaz de variados tipos de tratamento automático de informações ou processamento de dados. Entende se por computador um sistema físico que realiza algum tipo de computação. Assumiu se que os computadores pessoais e laptops são ícones da era da informação . O primeiro computador eletromecânico foi construído por Konrad Zuse (1910 1995). Atualmente, um microcomputador é também chamado computador pessoal ou ainda computador doméstico.”

## Máquina de Mealy

Implementar um transdutor finito (máquina de Moore ou Mealy) que, dada uma sequência de moedas de 25 e 50 centavos e de 1 real, forneça uma lata de refrigerante quando a sequência totalizar 1 real ou mais. Cada moeda inserida deverá corresponder a uma de duas saídas: 0, se uma lata não pode ser (ainda) liberada, ou 1, se u ma lata deve ser liberada. Exemplo:

| Entrada: | 50 | 25 | 50 | 100 | 25 | 50 | 10 | ... |
|:--------:|:--:|:--:|:--:|:---:|:--:|:--:|:--:|:---:|
|  Saída:  |  0 |  0 |  1 |  1  |  0 |  1 |  1 | ... |

\begin{figure}[ht]
\centering
\begin{tikzpicture}[scale=0.2]
\tikzstyle{every node}+=[inner sep=0pt]
\draw [black] (22.7,-30.5) circle (3);
\draw (22.7,-30.5) node {$q0$};
\draw [black] (22.7,-30.5) circle (2.4);
\draw [black] (38.3,-20.2) circle (3);
\draw (38.3,-20.2) node {$q1$};
\draw [black] (38.3,-20.2) circle (2.4);
\draw [black] (39.1,-41.4) circle (3);
\draw (39.1,-41.4) node {$q2$};
\draw [black] (39.1,-41.4) circle (2.4);
\draw [black] (52.9,-30.5) circle (3);
\draw (52.9,-30.5) node {$q3$};
\draw [black] (52.9,-30.5) circle (2.4);
\draw [black] (20.02,-31.823) arc (324:36:2.25);
\draw (15.45,-30.5) node [left] {$100\mbox{ }/\mbox{ }1$};
\fill [black] (20.02,-29.18) -- (19.67,-28.3) -- (19.08,-29.11);
\draw [black] (36.977,-17.52) arc (234:-54:2.25);
\draw (38.3,-12.95) node [above] {$100\mbox{ }/\mbox{ }1$};
\fill [black] (39.62,-17.52) -- (40.5,-17.17) -- (39.69,-16.58);
\draw [black] (55.58,-29.177) arc (144:-144:2.25);
\draw (60.15,-30.5) node [right] {$100\mbox{ }/\mbox{ }1$};
\fill [black] (55.58,-31.82) -- (55.93,-32.7) -- (56.52,-31.89);
\draw [black] (40.423,-44.08) arc (54:-234:2.25);
\draw (39.1,-48.65) node [below] {$100\mbox{ }/\mbox{ }1$};
\fill [black] (37.78,-44.08) -- (36.9,-44.43) -- (37.71,-45.02);
\draw [black] (25.2,-28.85) -- (35.8,-21.85);
\fill [black] (35.8,-21.85) -- (34.85,-21.88) -- (35.4,-22.71);
\draw (27.72,-24.85) node [above] {$25\mbox{ }/\mbox{ }0$};
\draw [black] (25.2,-32.16) -- (36.6,-39.74);
\fill [black] (36.6,-39.74) -- (36.21,-38.88) -- (35.66,-39.71);
\draw (33.68,-35.45) node [above] {$50\mbox{ }/\mbox{ }0$};
\draw [black] (41.45,-39.54) -- (50.55,-32.36);
\fill [black] (50.55,-32.36) -- (49.61,-32.46) -- (50.23,-33.25);
\draw (48.78,-36.45) node [below] {$25\mbox{ }/\mbox{ }0$};
\draw [black] (41.132,-21.186) arc (67.6508:41.94484:27.204);
\fill [black] (51.02,-28.16) -- (50.86,-27.23) -- (50.12,-27.9);
\draw (49.25,-23.62) node [above] {$50\mbox{ }/\mbox{ }0$};
\draw [black] (36.145,-40.897) arc (-103.76015:-143.45859:20.93);
\fill [black] (24.31,-33.03) -- (24.38,-33.97) -- (25.19,-33.37);
\draw (26.76,-38.5) node [below] {$50\mbox{ }/\mbox{ }1$};
\draw [black] (50.215,-29.163) arc (-118.22377:-132.1806:49.129);
\fill [black] (40.46,-22.28) -- (40.72,-23.19) -- (41.39,-22.45);
\draw (42.35,-26.52) node [below] {$50\mbox{ }/\mbox{ }1$};
\draw [black] (38.41,-23.2) -- (38.99,-38.4);
\fill [black] (38.99,-38.4) -- (39.46,-37.58) -- (38.46,-37.62);
\draw (38.14,-30.81) node [left] {$25\mbox{ }/\mbox{ }0$};
\draw [black] (21.689,-27.68) arc (194.55032:-14.55032:16.644);
\fill [black] (21.69,-27.68) -- (21.97,-26.78) -- (21,-27.03);
\draw (37.8,-6.35) node [above] {$25\mbox{ }/\mbox{ }1$};
\draw [black] (19.2,-36.2) -- (21.13,-33.06);
\fill [black] (21.13,-33.06) -- (20.29,-33.48) -- (21.14,-34);
\end{tikzpicture}
\caption{Máquina de Mealy do problema de retirada de latas de refrigerante.}
\label{fig:mealy}
\end{figure}