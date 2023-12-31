#!/usr/bin/perl
use strict;
use warnings;
use CGI;

print "Content-type: text/html\n\n";
print <<HTML;
<!DOCTYPE html>
<html>
  <head> 
    <meta charset="utf-8"> 
    <link rel="stylesheet" type="text/css" href="../css/style.css">
    <title>Resultado de Calculadora</title>
  </head>
<body>
HTML

my $q = CGI->new;
my $operation = $q->param("operation");

if($operation =~ /^[0-9]+.[+-*/][0-9]+$/){
    print "<h1>Operación válida</h1>";
}else{
    print "<h1>Operación no válida</h1>";
}
print <<HTML;
    Click <a href="../index.html">aqui</a> para regresar a la calculadora
</body>
</html>
HTML
