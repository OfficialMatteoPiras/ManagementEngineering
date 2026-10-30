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
  forall(j in v)
    sum(h in w) x[j][h] == 1;

  forall(h in w)
    sum(j in v) t[j]*x[j][h] <= TC;

  forall(d in P)
    sum(s in w) s*x[d.h1][s] <= sum(s in w) s*x[d.j1][s];

  forall(h in w)
    IT >= TC - sum(j in v) t[j]*x[j][h];
}

execute ShowSolution {
  writeln("Idle time massimo: " + IT);
  for(var j in v)
    for(var h in w)
      if(x[j][h] > 0.5)
        writeln("task " + j + " assegnato alla stazione " + h);
  for(var h in w) {
    var counter = 0;
    for(var j in v)
      if(x[j][h] > 0.5)
        counter = counter + t[j];
    writeln("tempo totale stazione " + h + ": " + counter);
  }
}
 