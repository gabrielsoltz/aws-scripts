# Assume Role using AWS CLI, one command:

export $(printf "AWS_ACCESS_KEY_ID=%s AWS_SECRET_ACCESS_KEY=%s AWS_SESSION_TOKEN=%s" \
$(aws sts assume-role \
--role-session-name ThisSession \
--query "Credentials.[AccessKeyId,SecretAccessKey,SessionToken]" \
--role-arn <<ROLE>> \
--output text))
