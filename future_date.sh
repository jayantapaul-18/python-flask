#!/bin/bash
#!/bin/bash
# Get the current date
current_date=$(date +%Y-%m-%d)
echo $current_date
# Get the expiration date
expiration_date=$(date "+30 days")
echo $expiration_date
# Calculate the future date
future_date=$(date "$expiration_date - 1 month" +%Y-%m-%d)
# Print the future date
echo "The future date is $future_date"
