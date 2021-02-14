<?php
$output = null;
$ejecucion = exec("/var/www/html/practica_php/euler/e18.py", $output);

echo "Camino: $output[2]";
echo "<br>";
echo "Suma total: $output[3]";
$nodos = explode(" ", $output[0]);
$camino = str_replace(array("[", "]"), "", $output[2]);
$camino = explode(", ", $camino);
$niveles = $output[1];
$numnodo = 0;
$p = 0;
$paso = 0;
echo "<div style='text-align:center;'>";
for ($n=0;$n<$niveles;$n++) {
  $numnodos = $n+1;
  for ($i=$nodo;$i<$numnodos;$i++) {
    if ($camino[$paso] == $p) {
      echo "<span style='color:red;'>"."$nodos[$numnodo]"."</span>";
      $paso = $paso+1;
    }
    else {
      echo "$nodos[$numnodo]";
    }
    echo "&nbsp;";
    $total = $total+$i;
    $p = $p+1;
    $numnodo = $numnodo+1;
  }
  $k = $k+1;
  $total = $total+1;
  echo "<br>";
}
echo "</div>";
?>
