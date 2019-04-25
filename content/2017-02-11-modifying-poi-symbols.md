Title: Modifying Viewranger Icons In Bulk
Date: 2017-02-11 11:16
Modified: 2017-02-11 11:16
Category: Articles
Tags: viewranger,  poi,  editing,  summits,  hill lists  
Author: Nick Bramhall
Summary: How to edit POI files to display different summits with a different symbol in Viewranger
Slug: modifying-poi-symbols

With the ever increasing number of hill lists out in the world, displaying summits as Points of Interest (POI) on your mapping app can be confusing. In Viewranger, if you don't make any changes then all summits, whether they are a 3,000 ft Munro or a lowly HuMP will show as a blue ball. It would be more useful to be able to identify different summit types by colour. There is a way to do this but unfortunately it requires a bit of effort with a text editor; as far as I can tell, it is not currently possible to make these changes via either Viewranger's web or app interface.

First of all download your POI file for the hill list in question (it's easier to do this on a list-by-list basis before combining into a single POI import once you have made the changes). For Viewranger this comes in the form of a .gpx file with each entry being an individual summit. If you open this file in a text editor you'll see a long list of entries, each one covering a different summit with all the details necassary to display it in Viewranger. 

Here is an example entry:

``` <wpt lat="56.96563" lon="-6.314678"><ele>0781.0</ele><name><![CDATA[Ainshval]]></name><cmt><![CDATA[Ainshval]]></cmt><desc><![CDATA[Ainshval]]></desc><sym>filled circle</sym></wpt> ```

The key bit of information for our purpose is the following snippet:

``` <sym>filled circle</sym> ```

This specifies the symbol used when displaying the POI. In this case, the generic filled circle has been chosen. We need to replace this with something different, for example:

``` <sym>Red ball</sym> ```

Now, this is quick to do if there is only one entry to change, however, hill lists typically contain a few hundred entries and modifying each by hand would be tedious. Instead, use your favourite text editor to do a **find and replace all** operation:

``` Find: <sym>filled circle</sym> ```
``` Replace with: <sym>Red ball</sym> ```

This will change each entry to use the red circle symbol. You can now save the file and then import it into Viewranger (if doing more than one list, make the *sym* changes and then copy and paste all the entries into a single master file for import). Trial and error may be required to get the symbols right, especially if you want to see more then two or three summit types.

In my Viewranger I have the following set:

* Munros in Red - <sym>Red ball</sym>
* Munro Tops in Purple - <sym>Purple ball</sym>
* Corbetts in Green - <sym>Green ball</sym>
* Grahams in Blue - <sym>Blue ball</sym>

<a href='https://photos.google.com/share/AF1QipNGRhkQP6GDdDzYczdWtOlP18iWenqEAOTD37EBEf6aYOAgV1OJTmsfr8v7WKY0IQ?key=NWtqY05pYlM2WGhsU0hTbDExbDNfTE5rbGMxalBB&source=ctrlq.org'><img src='https://lh3.googleusercontent.com/aXf8atkIJynPt-vBu4Na8-0MRXzs7FtRN_-GXyG3OJzk7GAssT31-LsmN2btPiJ11FTlLFf5y-G9xKxBH2mYIhhkrd4KtxUllWm9593SS3NyhLJoTWAyUes4-fEymwqmxQKz-Eg' /></a>

