/*********************************************
 * OPL 22.2.0.0 Model
 * Author: mattp
 * Creation Date: 29 Oct 2026 at 16:47:29
 *********************************************/

int n = ...;
range v = 1..n;
float t[v] = ...;
int k = ...;
range w = 1..k;
float TC = ...;

tuple A {
  int h1;
  int j1;
}
{A} P = ...;

dvar boolean x[v][w];
dvar float+ IT;

minimize IT;

subject to {
  // occorrenza: ogni task in una sola stazione
  forall(j in v)
    sum(h in w) x[j][h] == 1;

  // tempo ciclo
  forall(h in w)
    sum(j in v) t[j]*x[j][h] <= TC;

  // precedenze
  forall(d in P)
    sum(s in w) s*x[d.h1][s] <= sum(s in w) s*x[d.j1][s];

  // IT = massimo idle time tra le stazioni
  forall(h in w)
    IT >= TC - sum(j in v) t[j]*x[j][h];
}

execute ShowSolution {
  writeln("Idle time massimo: " + Opl.round(IT*100)/100);
  for(var h in w) {
    var counter = 0;
    var lista = "";
    for(var j in v) {
      if(x[j][h] > 0.5) {
        counter = counter + t[j];
        lista = lista + j + " ";
      }
    }
    writeln("Stazione " + h + ": task " + lista + "| tempo totale = " + Opl.round(counter*100)/100);
  }
}
 