PYTHON ?= python

check : \
	lal_verify \
	test_pidfile \
	test_pipeline \
	;
	@echo "All Tests Passed"

define printpassfail
	{ echo "Pass" ; true ; } || { echo "Fail" ; false ; }
endef

%: %.py
	@echo "=== start $@ ===>"
	$(PYTHON) $< && $(printpassfail)
	@echo "<=== end $@ ==="
