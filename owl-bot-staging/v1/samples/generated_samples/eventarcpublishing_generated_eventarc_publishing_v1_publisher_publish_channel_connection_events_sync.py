# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for PublishChannelConnectionEvents
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-eventarc-publishing


# [START eventarcpublishing_generated_eventarc_publishing_v1_Publisher_PublishChannelConnectionEvents_sync]
from google.cloud import eventarc_publishing_v1


def sample_publish_channel_connection_events():
    # Create a client
    client = eventarc_publishing_v1.PublisherClient()

    # Initialize request argument(s)
    request = eventarc_publishing_v1.PublishChannelConnectionEventsRequest(
    )

    # Make the request
    response = client.publish_channel_connection_events(request=request)

    # Handle response
    print(response)

# [END eventarcpublishing_generated_eventarc_publishing_v1_Publisher_PublishChannelConnectionEvents_sync]
