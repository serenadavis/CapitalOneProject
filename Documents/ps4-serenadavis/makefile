all: expression expression_tests

expression: expression.ml
	ocamlbuild -use-ocamlfind expression.byte

expression_tests: expression_tests.ml
	ocamlbuild -use-ocamlfind expression_tests.byte

clean:
	rm -rf _build *.byte