# Define default TASK
TASK = task1

# Define TASK_INPUT_TXT_PATH
TASK_INPUT_TXT_PATH = $(TASK)-input.txt

# Define TASK_ARTIFACTS_PATH
TASK_ARTIFACTS_PATH = $(TASK)-artifacts

# Define TASK_SCRIPT_PATH
TASK_SCRIPT_PATH = $(TASK).py

all:

test: $(TASK_SCRIPT) $(TASK_INPUT_TXT)
	@/usr/bin/time -f "Elapsed time in seconds: %e" \
		/bin/sh -c './$(TASK_SCRIPT_PATH) < $(TASK_INPUT_TXT_PATH)'

clean:
	rm $(TASK_ARTIFACTS_PATH)/* || true
