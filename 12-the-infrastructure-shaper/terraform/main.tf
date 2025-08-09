# Copyright 2025 Google LLC.
# SPDX-License-Identifier: Apache-2.0

# This is a simple Terraform configuration for demonstration purposes.
# It uses the 'local' provider to create a local file,
# which makes it easy to run without needing cloud credentials.

resource "local_file" "example" {
  content  = "This file was created by the Infrastructure Shaper persona."
  filename = "${path.module}/example.txt"
}
