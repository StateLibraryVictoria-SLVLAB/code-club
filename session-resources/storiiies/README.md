# Storiiies workshop

Storiiies is an open-source tool created by [Cogapp](https://www.cogapp.com/) that allows users to create visual, interactive stories from any image. Here is a link to the R+D page for Storiiies [https://www.cogapp.com/r-d/storiiies](https://www.cogapp.com/r-d/storiiies).

The Storiiies editor makes use of the International Image Interoperability Framework (IIIF) to create a *manifest* that records the image regions and any accompanying descriptions generated when creating a story.

## Retrieve a IIIF image URL for a State Library digital image

For a variety of reasons, the URL that a user sees when viewing a collection image on the State Library Victoria website does not directly relate to its IIIF resource. To help expose the IIIF URL, you can follow the instructions on this simple widget [https://statelibraryvictoria.github.io/url-retriiiever/](https://statelibraryvictoria.github.io/url-retriiiever/).

Once you have retrieved a valid IIIF URL you can start exploring some IIIF-powered tools:

### Storiiies

Head over to the Storiiies editor [https://storiiies-editor.cogapp.com/](https://storiiies-editor.cogapp.com/) and fill out the form by adding the IIIF image URL to the *IIIF manifest or info.json* box and filling out the rest of the form.

**Note:** if you use an SLV email account it is likely that the automated email from the Storiiies editor will land in your *junk* folder. However, it's important to retrieve it because it will contain a link to your story that enables you to edit and share the completed version.

### Explore the IIIF Image API

If you're interested in understanding a bit more about the Image API, then there's really useful *API playground* resource that let's you update the different URL query parameters and see the results in the browser [https://www.learniiif.org/image-api/playground](https://www.learniiif.org/image-api/playground).

## Links to interesting IIIF things

- the IIIF homepage has a plethora of useful information, including demos, learning resources and a calendar of community events [https://iiif.io/](https://iiif.io/)
- Mirador is one of the major IIIF compatible image viewers [https://projectmirador.org/](https://projectmirador.org/)
- Universal viewer is the other one [https://universalviewer.io/](https://universalviewer.io/)
- *Slow looking* is another tool created by Cogapp that aims to emulate the experience of getting up-close to a picture in a gallery [https://slowlooking.cogapp.com/](https://slowlooking.cogapp.com/)
- the David Rumsey Map Collection has created a Chrome browser extension that will add a random map from the collection to the background of a newly opened tab [https://chromewebstore.google.com/detail/david-rumsey-map-collecti/fnheacjohhlddiffbmafmpoblbkfgmde?pli=1](https://chromewebstore.google.com/detail/david-rumsey-map-collecti/fnheacjohhlddiffbmafmpoblbkfgmde?pli=1)
