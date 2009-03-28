<?xml version="1.0" encoding="Shift_JIS" ?>
<?xml-stylesheet href="rss.xml" type="text/xsl" media="screen"?>
<rdf:RDF 
  xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" 
  xmlns:content="http://purl.org/rss/1.0/modules/content/"
  xmlns:dc="http://purl.org/dc/elements/1.1/"
  xmlns="http://purl.org/rss/1.0/"
  xml:lang="ja">
  <channel rdf:about="[% rsstarget %][% rssfile %]">
    <title>もじら組forum - Updates</title>
    <link>[% rsstarget %]</link>
    <dc:title>もじら組forums</dc:title>
    <dc:creator>もじら組</dc:creator>
    <dc:date>$time</dc:date>
    <dc:language>ja</dc:language>
    <dc:rights rdf:resource="[% rsstarget %]"/>
    <description>もじら組forum更新情報</description>
    <items>
      <rdf:Seq>
      [% FOREACH item = items %]
        <rdf:li rdf:resource="[% rsstarget %]?mode=one&amp;namber=[% item.nam %]&amp;type=[% item.ty %]&amp;space=[% item.sp %]"/>
      [% END %]
      </rdf:Seq>
    </items>
  </channel>
  [% FOREACH item = items %]
  <item rdf:about="[% rsstarget %]?mode=one&amp;namber=[% item.nam %]&amp;type=[% item.ty %]&amp;space=[% item.sp %]">
    <title>[% item.d_may %]</title>
    <link>[% rsstarget %]?mode=one&amp;namber=[% item.nam %]&amp;type=[% item.ty %]&amp;space=[% item.sp %]</link>
    <description>[% item.desc %]</description>
    <content:encoded><![CDATA[[% item.content %]]]></content:encoded>
    <dc:name>[% item.name %]</dc:name>
    <dc:creator>[% item.name %]</dc:creator>
    <dc:date>[% item.time %]</dc:date>
  </item>
  [% END %]
</rdf:RDF>

