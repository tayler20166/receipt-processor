IMAGE_NAME=ak-python-test

ifeq ($(OS),Windows_NT)
    OS := Windows
else
    OS := $(shell uname -s)
endif

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run -d -p 80:80 -p 8080:8080 $(IMAGE_NAME)

stop:
ifeq ($(OS),Linux)
	@echo "Stopping and removing all containers based on the $(IMAGE_NAME) image... (Linux)"
	@docker ps -q --filter "ancestor=$(IMAGE_NAME)" | xargs -r docker stop
	@docker ps -aq --filter "ancestor=$(IMAGE_NAME)" | xargs -r docker rm
else ifeq ($(OS),Darwin)
	@echo "Stopping and removing all containers based on the $(IMAGE_NAME) image... (macOS)"
	@docker ps -q --filter "ancestor=$(IMAGE_NAME)" | xargs -r docker stop
	@docker ps -aq --filter "ancestor=$(IMAGE_NAME)" | xargs -r docker rm
else
	@echo "Stopping and removing all containers based on the $(IMAGE_NAME) image... (Windows)"
	@"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -Command "docker ps -q --filter 'ancestor=$(IMAGE_NAME)' | ForEach-Object {docker stop $$PSItem}"
	@"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -Command "docker ps -aq --filter 'ancestor=$(IMAGE_NAME)' | ForEach-Object {docker rm $$PSItem}"

endif

clean:
	docker rmi $(IMAGE_NAME)

.PHONY: build run stop clean