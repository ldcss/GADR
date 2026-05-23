## ADR 7: Publishing with ClickOnce
July 26, 2019

### Context
The app needs a convenient way to deploy to multiple devices. However this is done, installing and updating the app should be effortless for users. Ideally, the developer would make any necessary changes to the app, publish those changes to a location, and someone on the other end would only need to double click a download/update link.

### Decision
Older WPF and WinForm applications used a separate setup application, which was responsible for guiding someone through the process of installing an app. A user first downloaded the setup application, which would be responsible for installing the separate application on a system. We abandoned this route early in the development process due to the frequent errors that occurred during the install process.

ClickOnce is the standard publishing method for WPF applications. Visual studio even references ClickOnce under the "Security" tab of the properties window. Documentation on ClickOnce is also quite robust. Because of this, we will accept ClickOnce as our method of choice when publishing.

### Status
Accepted

### Consequences
There aren't many options to choose from when it comes to deploying a WPF application. Unfortunately, if ClickOnce doesn't easily suit our needs, we'll likely have to spend a good bit of time troubleshooting.

_In Retrospect:_ Unfortunately, it is recommended that ClickOnce deploys to a CD-Rom, a website, or a file share/UNC path. This seems particularly dated, especially with the CD-Rom reference. Also, the Adler Planetarium is deprecating their local file share system in lieu of using Google Drive. This is why we use Google Drive File Stream (see wiki) when publishing, which works _fine_. As WPF isn't necessarily cutting-edge technology, I don't see the publishing process evolving much in the future. While ClickOnce _usually_ works well, we'll have to deal with any errors in deployment as we have our hands tied with using ClickOnce.
