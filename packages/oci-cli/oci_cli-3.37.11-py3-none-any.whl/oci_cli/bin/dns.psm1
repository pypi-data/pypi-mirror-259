function GetOciTopLevelCommand_dns() {
    return 'dns'
}

function GetOciSubcommands_dns() {
    $ociSubcommands = @{
        'dns' = 'record resolver resolver-endpoint steering-policy steering-policy-attachment tsig-key view zone zone-transfer-server'
        'dns record' = 'domain rrset zone'
        'dns record domain' = 'delete get patch update'
        'dns record rrset' = 'delete get patch update'
        'dns record zone' = 'get patch update'
        'dns resolver' = 'change-compartment get list update'
        'dns resolver-endpoint' = 'create delete get list update'
        'dns steering-policy' = 'change-compartment create delete get list update'
        'dns steering-policy-attachment' = 'create delete get list update'
        'dns tsig-key' = 'change-compartment create delete get list update'
        'dns view' = 'change-compartment create delete get list update'
        'dns zone' = 'change-compartment create create-zone-from-zone-file delete get get-zone-content list migrate-from-dynect update'
        'dns zone-transfer-server' = 'list'
    }
    return $ociSubcommands
}

function GetOciCommandsToLongParams_dns() {
    $ociCommandsToLongParams = @{
        'dns record domain delete' = 'compartment-id domain force from-json help if-match if-unmodified-since scope view-id zone-name-or-id'
        'dns record domain get' = 'all compartment-id domain from-json help if-modified-since if-none-match limit page page-size rtype scope sort-by sort-order view-id zone-name-or-id zone-version'
        'dns record domain patch' = 'compartment-id domain from-json help if-match if-unmodified-since items scope view-id zone-name-or-id'
        'dns record domain update' = 'compartment-id domain force from-json help if-match if-unmodified-since items scope view-id zone-name-or-id'
        'dns record rrset delete' = 'compartment-id domain force from-json help if-match if-unmodified-since rtype scope view-id zone-name-or-id'
        'dns record rrset get' = 'all compartment-id domain from-json help if-modified-since if-none-match limit page page-size rtype scope view-id zone-name-or-id zone-version'
        'dns record rrset patch' = 'compartment-id domain from-json help if-match if-unmodified-since items rtype scope view-id zone-name-or-id'
        'dns record rrset update' = 'compartment-id domain force from-json help if-match if-unmodified-since items rtype scope view-id zone-name-or-id'
        'dns record zone get' = 'all compartment-id domain domain-contains from-json help if-modified-since if-none-match limit page page-size rtype scope sort-by sort-order view-id zone-name-or-id zone-version'
        'dns record zone patch' = 'compartment-id from-json help if-match if-unmodified-since items scope view-id zone-name-or-id'
        'dns record zone update' = 'compartment-id force from-json help if-match if-unmodified-since items scope view-id zone-name-or-id'
        'dns resolver change-compartment' = 'compartment-id from-json help if-match resolver-id scope'
        'dns resolver get' = 'from-json help if-modified-since if-none-match resolver-id scope'
        'dns resolver list' = 'all compartment-id display-name from-json help id lifecycle-state limit page page-size scope sort-by sort-order'
        'dns resolver update' = 'attached-views defined-tags display-name force freeform-tags from-json help if-match if-unmodified-since max-wait-seconds resolver-id rules scope wait-for-state wait-interval-seconds'
        'dns resolver-endpoint create' = 'forwarding-address from-json help is-forwarding is-listening listening-address max-wait-seconds name nsg-ids resolver-id scope subnet-id wait-for-state wait-interval-seconds'
        'dns resolver-endpoint delete' = 'force from-json help if-match if-unmodified-since resolver-endpoint-name resolver-id scope'
        'dns resolver-endpoint get' = 'from-json help if-modified-since if-none-match resolver-endpoint-name resolver-id scope'
        'dns resolver-endpoint list' = 'all from-json help lifecycle-state limit name page page-size resolver-id scope sort-by sort-order'
        'dns resolver-endpoint update' = 'force from-json help if-match if-unmodified-since max-wait-seconds nsg-ids resolver-endpoint-name resolver-id scope wait-for-state wait-interval-seconds'
        'dns steering-policy change-compartment' = 'compartment-id from-json help if-match scope steering-policy-id'
        'dns steering-policy create' = 'answers compartment-id defined-tags display-name freeform-tags from-json health-check-monitor-id help max-wait-seconds rules scope template ttl wait-for-state wait-interval-seconds'
        'dns steering-policy delete' = 'force from-json help if-match if-unmodified-since max-wait-seconds scope steering-policy-id wait-for-state wait-interval-seconds'
        'dns steering-policy get' = 'from-json help if-modified-since if-none-match scope steering-policy-id'
        'dns steering-policy list' = 'all compartment-id display-name display-name-contains from-json health-check-monitor-id help id lifecycle-state limit page page-size scope sort-by sort-order template time-created-greater-than-or-equal-to time-created-less-than'
        'dns steering-policy update' = 'answers defined-tags display-name force freeform-tags from-json health-check-monitor-id help if-match if-unmodified-since max-wait-seconds rules scope steering-policy-id template ttl wait-for-state wait-interval-seconds'
        'dns steering-policy-attachment create' = 'display-name domain-name from-json help max-wait-seconds scope steering-policy-id wait-for-state wait-interval-seconds zone-id'
        'dns steering-policy-attachment delete' = 'force from-json help if-match if-unmodified-since max-wait-seconds scope steering-policy-attachment-id wait-for-state wait-interval-seconds'
        'dns steering-policy-attachment get' = 'from-json help if-modified-since if-none-match scope steering-policy-attachment-id'
        'dns steering-policy-attachment list' = 'all compartment-id display-name domain domain-contains from-json help id lifecycle-state limit page page-size scope sort-by sort-order steering-policy-id time-created-greater-than-or-equal-to time-created-less-than zone-id'
        'dns steering-policy-attachment update' = 'display-name from-json help if-match if-unmodified-since max-wait-seconds scope steering-policy-attachment-id wait-for-state wait-interval-seconds'
        'dns tsig-key change-compartment' = 'compartment-id from-json help if-match scope tsig-key-id'
        'dns tsig-key create' = 'algorithm compartment-id defined-tags freeform-tags from-json help max-wait-seconds name scope secret wait-for-state wait-interval-seconds'
        'dns tsig-key delete' = 'force from-json help if-match if-unmodified-since max-wait-seconds scope tsig-key-id wait-for-state wait-interval-seconds'
        'dns tsig-key get' = 'from-json help if-modified-since if-none-match scope tsig-key-id'
        'dns tsig-key list' = 'all compartment-id from-json help id lifecycle-state limit name page page-size scope sort-by sort-order'
        'dns tsig-key update' = 'defined-tags force freeform-tags from-json help if-match if-unmodified-since max-wait-seconds scope tsig-key-id wait-for-state wait-interval-seconds'
        'dns view change-compartment' = 'compartment-id from-json help if-match scope view-id'
        'dns view create' = 'compartment-id defined-tags display-name freeform-tags from-json help max-wait-seconds scope wait-for-state wait-interval-seconds'
        'dns view delete' = 'force from-json help if-match if-unmodified-since max-wait-seconds scope view-id wait-for-state wait-interval-seconds'
        'dns view get' = 'from-json help if-modified-since if-none-match scope view-id'
        'dns view list' = 'all compartment-id display-name from-json help id lifecycle-state limit page page-size scope sort-by sort-order'
        'dns view update' = 'defined-tags display-name force freeform-tags from-json help if-match if-unmodified-since max-wait-seconds scope view-id wait-for-state wait-interval-seconds'
        'dns zone change-compartment' = 'compartment-id from-json help if-match scope zone-id'
        'dns zone create' = 'compartment-id defined-tags external-downstreams external-masters freeform-tags from-json help max-wait-seconds name scope view-id wait-for-state wait-interval-seconds zone-type'
        'dns zone create-zone-from-zone-file' = 'compartment-id create-zone-from-zone-file-details from-json help scope view-id'
        'dns zone delete' = 'compartment-id force from-json help if-match if-unmodified-since max-wait-seconds scope view-id wait-for-state wait-interval-seconds zone-name-or-id'
        'dns zone get' = 'compartment-id from-json help if-modified-since if-none-match scope view-id zone-name-or-id'
        'dns zone get-zone-content' = 'file from-json help if-modified-since if-none-match scope view-id zone-name-or-id'
        'dns zone list' = 'all compartment-id from-json help lifecycle-state limit name name-contains page page-size scope sort-by sort-order time-created-greater-than-or-equal-to time-created-less-than tsig-key-id view-id zone-type'
        'dns zone migrate-from-dynect' = 'compartment-id defined-tags dynect-migration-details freeform-tags from-json help max-wait-seconds name scope view-id wait-for-state wait-interval-seconds'
        'dns zone update' = 'compartment-id defined-tags external-downstreams external-masters force freeform-tags from-json help if-match if-unmodified-since max-wait-seconds scope view-id wait-for-state wait-interval-seconds zone-name-or-id'
        'dns zone-transfer-server list' = 'all compartment-id from-json help page scope'
    }
    return $ociCommandsToLongParams
}

function GetOciCommandsToShortParams_dns() {
    $ociCommandsToShortParams = @{
        'dns record domain delete' = '? c h'
        'dns record domain get' = '? c h'
        'dns record domain patch' = '? c h'
        'dns record domain update' = '? c h'
        'dns record rrset delete' = '? c h'
        'dns record rrset get' = '? c h'
        'dns record rrset patch' = '? c h'
        'dns record rrset update' = '? c h'
        'dns record zone get' = '? c h'
        'dns record zone patch' = '? c h'
        'dns record zone update' = '? c h'
        'dns resolver change-compartment' = '? c h'
        'dns resolver get' = '? h'
        'dns resolver list' = '? c h'
        'dns resolver update' = '? h'
        'dns resolver-endpoint create' = '? h'
        'dns resolver-endpoint delete' = '? h'
        'dns resolver-endpoint get' = '? h'
        'dns resolver-endpoint list' = '? h'
        'dns resolver-endpoint update' = '? h'
        'dns steering-policy change-compartment' = '? c h'
        'dns steering-policy create' = '? c h'
        'dns steering-policy delete' = '? h'
        'dns steering-policy get' = '? h'
        'dns steering-policy list' = '? c h'
        'dns steering-policy update' = '? h'
        'dns steering-policy-attachment create' = '? h'
        'dns steering-policy-attachment delete' = '? h'
        'dns steering-policy-attachment get' = '? h'
        'dns steering-policy-attachment list' = '? c h'
        'dns steering-policy-attachment update' = '? h'
        'dns tsig-key change-compartment' = '? c h'
        'dns tsig-key create' = '? c h'
        'dns tsig-key delete' = '? h'
        'dns tsig-key get' = '? h'
        'dns tsig-key list' = '? c h'
        'dns tsig-key update' = '? h'
        'dns view change-compartment' = '? c h'
        'dns view create' = '? c h'
        'dns view delete' = '? h'
        'dns view get' = '? h'
        'dns view list' = '? c h'
        'dns view update' = '? h'
        'dns zone change-compartment' = '? c h'
        'dns zone create' = '? c h'
        'dns zone create-zone-from-zone-file' = '? c h'
        'dns zone delete' = '? c h'
        'dns zone get' = '? c h'
        'dns zone get-zone-content' = '? h'
        'dns zone list' = '? c h'
        'dns zone migrate-from-dynect' = '? c h'
        'dns zone update' = '? c h'
        'dns zone-transfer-server list' = '? c h'
    }
    return $ociCommandsToShortParams
}