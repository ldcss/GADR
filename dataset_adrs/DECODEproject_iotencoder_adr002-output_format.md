# ADR002: Define an output format for data written to the datastore

## Context

The stream encoder component defined in this project is designed to subscribe
to the MQTT broker provided by SmartCitizen. This broker is used to support
SmartCitizen's existing platform and will not be modified specifically for
DECODE.

Events published via the broker look like this:

```json
{
  "data": [
    {
      "recorded_at": "2018-11-01T13:59:06Z",
      "sensors": [
        {
          "id": 10,
          "value": 0
        },
        {
          "id": 10,
          "value": 0
        },
        {
          "id": 14,
          "value": 0
        },
        {
          "id": 55,
          "value": 29.1
        },
        {
          "id": 56,
          "value": 36.64
        },
        {
          "id": 16,
          "value": 41.4
        }
      ]
    }
  ]
}
```

That is we receive a timestamp for the event, and then an array of readings
comprising an `id` (which is a numeric id that relates to specific sensor type
as described by SmartCitizen) and a numeric value.

Not included in the received event are the following fields:

* The location of the device
* The exposure of the device (indoor, outdoor)
* The name, description or units of received sensor measurements

Sensor id values are described by SmartCitizen via an API endpoint:
https://api.smartcitizen.me/v0/sensors

This returns JSON that looks like this:

```json
[
  {
    "id": 3,
    "uuid": "ac284ba3-e2fc-4795-b2b1-530b32a9b05b",
    "parent_id": null,
    "name": "DHT22",
    "description": "A digital temperature and humidity sensor. It uses a capacitive humidity sensor and a thermistor to measure the surrounding air, and spits out a digital signal on the data pin (no analog input pins needed)",
    "unit": null,
    "created_at": "2015-02-02T18:14:15Z",
    "updated_at": "2015-02-02T18:14:15Z",
    "measurement": null
  },
  {
    "id": 20,
    "uuid": "4a2e9c80-748c-44a3-b400-8824f50d19cd",
    "parent_id": null,
    "name": "MiCS4514",
    "description": "Gas Sensor",
    "unit": null,
    "created_at": "2015-02-02T18:31:50Z",
    "updated_at": "2015-02-02T18:31:50Z",
    "measurement": null
  }
]
```

So it is this JSON that encodes all metadata about each sensor including names,
descriptions and units.

### Constraints

### Options

We identified the following options:

* The encoder could encrypt the data exactly as received to the encrypted
  datastore, meaning that when the receiving dashboard fetches and decrypts the
  data it will have to make a request to the SmartCitizen API to convert the
  numerical sensor IDs into something more meaningful to know how to represent
  the data.

  This fetching of data from the SmartCitizen API could happen every time the
  dashboard scrapes data from the encrypted datastore, or it could be updated
  to include a local copy of the sensor ID mappings.

* The encoder could enrich the data, so that the data that is then written to
  the datastore has locations, and sensor metadata added directly to the file
  meaning that the receiver can immediately understand the data in order to
  render it appropriately.

  Note that again here we could add this enriching metadata dynamically on
  every request, by fetching from the SmartCitizen API, or by caching a local
  copy of the sensor mappings such that this information is already known to
  the encoder.

## Decision

We will enrich the data within the encoder using a cached copy of
SmartCitizen's sensor JSON.

Reasoning:

* Removes any coupling between the final receipient of the data and
  SmartCitizen. This avoids consumers having to build knowledge of the
  SmartCitizen API into their systems, and would be more scalable if other data
  sources were ever added.

* Sensor types included by SmartCitizen do not change frequently (last update
  was 2016, so 2 years ago at time of writing).  Because of this low update
  frequency there is likely to be little issue with having to update the local
  cached copy frequently.

The output JSON we will publish will look like this:

```json
{
  "longitude": 2.234,
  "latitude": 54.213,
  "exposure": "INDOOR",
  "recordedAt": "2018-11-01T15:06:23Z",
  "userUid": "abc-123-fbd",
  "sensors": [
    {
      "sensorId": 29,
      "name": "MEMS Mic",
      "description": "MEMS microphone with envelope follower sound pressure sensor (noise).",
      "unit": "dBC",
      "type": "SHARE",
      "value": 64.252
    },
    {
      "sensorId": 14,
      "name": "BH1730FVC",
      "description": "Digital Ambient Light Sensor",
      "unit": "Lux",
      "type": "BIN",
      "bins": [5,10,50,500],
      "values": [0,1,0,0,0]
    },
    {
      "sensorId": 4,
      "name": "HPP828E031",
      "description": "Temperature",
      "unit": "ºC",
      "type": "MOVING_AVG",
      "interval": 900,
      "value": 18.2
    }
  ]
}
```
