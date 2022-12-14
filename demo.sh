#!/bin/bash
cookiecutter --no-input --config-file config.yaml git@github.com:alexrashed/cookiecutter-ls-oa-ext.git
cp code/* localstack-christmas-countdown/localstack_christmas_countdown/controllers
