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
my $answer = 0;

if($operation =~ /^[0-9]+[\+\-\*\/][0-9]+$/){
    if($operation =~ /^([0-9]+)\+([0-9]+)$/){
        $answer = $1 + $2;
    }elsif($operation =~ /^([0-9]+)\-([0-9]+)$/){
        $answer = $1 - $2;
    }elsif($operation =~ /^([0-9]+)\*([0-9]+)$/){
        $answer = $1 * $2;
    }elsif($operation =~ /^([0-9]+)\/([0-9]+)$/){
        $answer = $1 / $2;
    }
    if(defined $answer){
        print "La respuesta es: $answer";
    }elsif{
        print "Respuesta no definida";
    }
}else{
    print "<h1>Operación no válida</h1>";
}
print <<HTML;
    Click <a href="../index.html">aqui</a> para regresar a la calculadora
</body>
</html>
HTML
