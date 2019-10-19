#!/usr/bin/env sh

export ENVIRONMENT
ENVIRONMENT=${ENVIRONMENT:-'staging'}

if [ $ENVIRONMENT == 'production' ]; then
  supervisord -c config/supervisord/deployment.prod.conf -n
elif [ $ENVIRONMENT == 'staging' ]; then
  supervisord -c config/supervisord/deployment.staging.conf -n
else
  supervisord -c config/supervisord/deployment.dev.conf -n
fi